from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm

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
    if req.method == "POST":
        u_form = UserUpdateForm(req.POST, instance=req.user)
        p_form = ProfileUpdateForm(req.POST, req.FILES, instance=req.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(req, f"User Updated")
            return redirect("usersProfile")
    else:
        u_form = UserUpdateForm(instance=req.user)
        p_form = ProfileUpdateForm(instance=req.user.profile)
    context = {"u_form": u_form, "p_form": p_form}
    return render(req, "users/profile.html", context)
