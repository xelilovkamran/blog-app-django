from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    name = models.CharField(max_length=250, null=True)
    email = models.EmailField(unique=True, null=True)
    avatar = models.ImageField(null=True, default='defaults/defaultAvatar.svg')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["username"]


class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

    class Meta:
        ordering = ['-created_at']


class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    category = models.ManyToManyField(Category, related_name='blogs')
    image = models.ImageField(
        null=True, default='defaults/defaultBlogImage.jpg')
    content = models.TextField()
    likes_count = models.PositiveIntegerField(default=0)
    liked_by = models.ManyToManyField(
        User, related_name='liked_posts', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ContactPage(models.Model):
    email = models.EmailField()
    location = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return "Contact Us"


class AboutPage(models.Model):
    company_name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return "About Us"
