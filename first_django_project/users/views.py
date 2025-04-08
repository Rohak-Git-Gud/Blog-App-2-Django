from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def usersRegister(req):
    form = UserCreationForm()
    return render(req, "users/register.html", {"form": form})
