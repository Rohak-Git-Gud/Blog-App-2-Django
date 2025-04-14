from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm

# from django.contrib.auth.forms import UserCreationForm


def usersRegister(req):
    if req.method == "POST":
        form = UserRegistrationForm(req.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")  # Temp.
            messages.success(req, f"User created. You can now Login")  # Temp.
            return redirect("usersLogin")
    else:
        form = UserRegistrationForm()
    return render(req, "users/register.html", {"form": form})


@login_required
def usersProfile(req):
    return render(req, "users/profile.html")
