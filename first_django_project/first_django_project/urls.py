"""
URL configuration for first_django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from users import views as userViews
from django.contrib.auth import views as authViews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", include("blog.urls")),
    path("register/", userViews.usersRegister, name="usersRegister"),  # Alt. Method; Temp.
    path("profile/", userViews.usersProfile, name="usersProfile"),
    path("login/", authViews.LoginView.as_view(template_name="users/login.html"), name="usersLogin"),  # Another Alt. Method
    path("logout/", authViews.LogoutView.as_view(template_name="users/logout.html"), name="usersLogout"),
    path("admin/", admin.site.urls),
]

# Deployment proofing
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
