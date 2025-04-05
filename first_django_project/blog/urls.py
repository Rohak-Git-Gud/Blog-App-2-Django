from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogHome, name="blogHome"),
    path('about/', views.blogAbout, name="blogAbout"),
]
