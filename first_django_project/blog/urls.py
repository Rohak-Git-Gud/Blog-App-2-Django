from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
)
from . import views

urlpatterns = [
    # path("", views.blogHome, name="blogHome"),
    path("about/", views.blogAbout, name="blogAbout"),
    path("post/create/", PostCreateView.as_view(), name="blogCreate"),
    path("", PostListView.as_view(), name="blogHome"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="blogRead"),
    path("user/<str:username>/", UserPostListView.as_view(), name="userBlogs"),
    path("post/update/<int:pk>/", PostUpdateView.as_view(), name="blogUpdate"),
    path("post/delete/<int:pk>/", PostDeleteView.as_view(), name="blogDelete"),
]
