from django.shortcuts import render

from django.http import HttpResponse
posts = [
    {
        "author": "R",
        "title": "One",
        "content": "1 - lorem ipsum",
        "date": "Today",
    },
    {
        "author": "S",
        "title": "Two",
        "content": "2 - lorem ipsum",
        "date": "Tomorrow",
    },
]


def blogHome(req):
    # Can send a dictionary of data as context
    context = {
        "posts": posts,
    }
    return render(req, "blog/home.html", context)
    # return render(req, "blog/home.html")
    # return HttpResponse("<h1>Blog Home</h1>")


def blogAbout(req):
    return render(req, "blog/about.html")
