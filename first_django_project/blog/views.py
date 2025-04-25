from django.shortcuts import render, get_object_or_404
from .models import Post
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# from django.http import HttpResponse
# posts = [
#     {
#         "author": "R",
#         "title": "One",
#         "content": "1 - lorem ipsum",
#         "date": "Today",
#     },
#     {
#         "author": "S",
#         "title": "Two",
#         "content": "2 - lorem ipsum",
#         "date": "Tomorrow",
#     },
# ]


def blogHome(req):
    context = {
        "posts": Post.objects.all(),
    }
    return render(req, "blog/home.html", context)
    # Can send a dictionary of data as context
    # context = {
    #     "posts": posts,
    # }
    # return render(req, "blog/home.html", context)

    # return render(req, "blog/home.html")

    # return HttpResponse("<h1>Blog Home</h1>")


def blogAbout(req):
    return render(req, "blog/about.html")


# CRUD


# C - Create
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# R - Retrieve all
class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"
    # Looks for <app>/<model>_<view_type>.html be default.
    context_object_name = "posts"
    ordering = ["-creation_date"]
    paginate_by = 4


# R - Retrieve one
class PostDetailView(DetailView):
    model = Post


# U - Update
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


# D - Delete
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


# Profile
class UserPostListView(ListView):
    model = Post
    template_name = "blog/user_posts.html"
    context_object_name = "posts"
    paginate_by = 4

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        return Post.objects.filter(author=user).order_by("-creation_date")
