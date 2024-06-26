from django.urls import path
from . import views

app_name = "base"

urlpatterns = [
    path("", views.home, name="home"),
    path("sign-in/", views.signIn, name="sign-in"),
    path("sign-up/", views.signUp, name="sign-up"),
    path("logout/", views.logoutUser, name="logout"),
    path("blog/<int:pk>/", views.showBlog, name="blog-details"),
    path("blog/create/", views.createBlog, name="create-blog"),
    path("blog/<int:pk>/like/", views.likeBlog, name="like-blog"),
    path("blog/<int:pk>/comment/", views.commentBlog, name="comment-blog"),
    path("blog/delete/<int:pk>", views.deleteBlog, name="delete-blog"),



    path('contact/', views.contact_us_view, name='contact_us'),
    path('about/', views.about_us_view, name='about_us'),
]
