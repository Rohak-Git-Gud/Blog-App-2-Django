from django.shortcuts import render
from django.http import HttpResponse


def blogHome(req):
    return HttpResponse("<h1>Blog Home</h1>")


def blogAbout(req):
    return HttpResponse("<h1>Blog About</h1>")
