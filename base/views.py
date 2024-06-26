from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth import authenticate, login, logout
from .models import User, Blog, Category, Comment, ContactPage, AboutPage
from .forms import MyUserCreatingForm
from django.contrib.auth.decorators import login_required
import json

# Create your views here.


def home(request):
    filterCategory = request.GET.get('category')
    if filterCategory == "all" or filterCategory is None:
        blogs = Blog.objects.all()
    else:
        blogs = Blog.objects.filter(category__name=filterCategory)

    categories = Category.objects.all()
    categoriesContent = {}

    for blog in blogs:
        blog.content = blog.content[:200] + '...'

    for category in categories:
        categoriesContent[category.name] = category.blogs.all().count()

    context = {
        'blogs': blogs,
        'categoriesContent': categoriesContent,
    }
    return render(request, 'base/home.html', context=context)


@login_required(login_url='base:sign-in')
def createBlog(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        categories = request.POST.getlist('category[]')
        image = request.FILES.get('banner')
        additional_categories = request.POST.get(
            'additioanlCategories')
        additional_categories = additional_categories.split(',')

        for add_category in additional_categories:
            if add_category != '':
                categories.append(add_category)

        if len(categories) == 0:
            categories = Category.objects.all()
            context = {'categories': categories,
                       'error': 'Please select a category'}
            return render(request, 'base/create-blog.html', context=context)

        if image is None:
            blog = Blog.objects.create(
                author=request.user,
                title=title,
                content=content,
            )
        else:
            blog = Blog.objects.create(
                author=request.user,
                title=title,
                content=content,
                image=image
            )

        for category in categories:
            category = Category.objects.get_or_create(name=category)[0]
            blog.category.add(category)

        return redirect('base:home')

    return render(request, 'base/create-blog.html', {'categories': categories})


@login_required(login_url='base:sign-in')
def deleteBlog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.delete()
    return HttpResponse(status=204, content_type='application/json',
                        data=json.dumps({'message': 'success'}))


def signIn(request):
    if request.user.is_authenticated:
        return redirect('base:home')

    if request.method == 'POST':
        email = request.POST['email'].lower()
        password = request.POST['password']
        try:
            user = User.objects.get(email=email)
        except:
            context = {"error": "User does not exist"}
            return render(request, 'base/sign-in.html', context=context)

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('base:home')
        else:
            context = {"error": "Invalid credentials"}
            return render(request, 'base/sign-in.html', context=context)

    return render(request, 'base/sign-in.html')


def signUp(request):
    if request.user.is_authenticated:
        return redirect('base:home')

    form = MyUserCreatingForm()

    if request.method == 'POST':
        form = MyUserCreatingForm(request.POST)
        if form.is_valid():
            form.save()
            login(request, form.instance)
            return redirect('base:home')
        else:
            context = {"form": form}
            return render(request, 'base/sign-up.html', context=context)

    return render(request, 'base/sign-up.html', {'form': form})


def logoutUser(request):
    logout(request)
    return redirect('base:home')


def showBlog(request, pk):
    blog = Blog.objects.get(pk=pk)
    comments = blog.comment_set.all()
    is_liked = blog.liked_by.filter(id=request.user.id).exists()
    like_count = blog.likes_count
    context = {'blog': blog, 'comments': comments,
               'is_liked': is_liked, 'like_count': like_count}
    return render(request, 'base/blog.html', context=context)


def commentBlog(request, pk):
    if not request.user.is_authenticated:
        return redirect('base:sign-in')

    if request.method == 'POST':
        message = request.POST.get('comment')
        blog = Blog.objects.get(pk=pk)
        comment = Comment.objects.create(
            author=request.user,
            blog=blog,
            content=message
        )
        blog.comment_set.add(comment)

    return redirect('base:blog-details', pk=pk)


def likeBlog(request, pk):
    blog = Blog.objects.get(pk=pk)
    if not request.user.is_authenticated:
        blog.likes_count += 1
        blog.save()
        return redirect('base:blog-details', pk=pk)

    if request.user in blog.liked_by.all():
        blog.liked_by.remove(request.user)
        blog.likes_count -= 1
    else:
        print('liked')
        blog.liked_by.add(request.user)
        blog.likes_count += 1

    blog.save()
    return redirect('base:blog-details', pk=pk)


def contact_us_view(request):
    page = ContactPage.objects.first()
    return render(request, 'base/contact.html', {'page': page, 'email': page.email})


def about_us_view(request):
    page = AboutPage.objects.first()
    return render(request, 'base/about.html', {'page': page})
