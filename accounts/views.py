from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import (
    login as auth_login,
    logout as auth_logout,
    authenticate,
)
from django.contrib.auth.decorators import login_required
from accounts.forms import (
    LoginForm,
    UserProfileCreationForm,
    UserCreationForm,
    UserChangeForm,
    EnterpriseCreationForm,
)
from ideas.forms import (
    IdeaForm,
)
from .models import UserProfile

from ideas.models import Idea

from django.forms import inlineformset_factory


@login_required
def logout(request):
    auth_logout(request)
    return redirect("index")


def login(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect("index")
    else:
        form = LoginForm()
    return render(request, "accounts/login.html", {"form": form})


def register(request):
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        user_profile_form = UserProfileCreationForm(request.POST)
        enterprise_form = EnterpriseCreationForm(request.POST)

        valid = user_form.is_valid() and user_profile_form.is_valid()
        if valid:
            role = user_profile_form.cleaned_data.get("role")
            if role == "entrepreneur":
                valid = valid and enterprise_form.is_valid()

        if valid:
            user = user_form.save()
            user_profile = user_profile_form.save(commit=False)
            user_profile.user = user
            user_profile.save()

            if user_profile.role == "entrepreneur":
                enterprise = enterprise_form.save(commit=False)
                enterprise.user_profile = user_profile
                enterprise.save()

            auth_login(
                request,
                user,
                backend="django.contrib.auth.backends.ModelBackend",
            )
            return redirect("accounts:profile")

    else:
        user_form = UserCreationForm()
        user_profile_form = UserProfileCreationForm()
        enterprise_form = EnterpriseCreationForm()

    return render(
        request,
        "accounts/register.html",
        {
            "user_form": user_form,
            "user_profile_form": user_profile_form,
            "enterprise_form": enterprise_form,
        },
    )


@login_required
def profile(request):
    if request.method == "POST":
        form = IdeaForm(request.POST)
        if form.is_valid():
            idea = form.save(commit=False)
            idea.user_profile = request.user.userprofile
            idea.save()
            return redirect("accounts:profile")
    else:
        form = IdeaForm()

    user_ideas = request.user.userprofile.ideas.all()

    user_investments = request.user.userprofile.investments.all()

    return render(
        request,
        "accounts/profile.html",
        {"form": form, "user_ideas": user_ideas, "user_investments": user_investments},
    )


@login_required
def edit_profile(request):
    if request.method == "POST":
        user_form = UserChangeForm(request.POST, instance=request.user)
        profile_form = UserProfileCreationForm(
            request.POST, instance=request.user.userprofile
        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("accounts:profile")
    else:
        user_form = UserChangeForm(instance=request.user)
        profile_form = UserProfileCreationForm(
            instance=request.user.userprofile
        )

    return render(
        request,
        "accounts/edit_profile.html",
        {"user_form": user_form, "profile_form": profile_form},
    )