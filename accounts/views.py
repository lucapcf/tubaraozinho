from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, redirect, render


from accounts.forms import (
    EnterpriseCreationForm,
    LoginForm,
    UserChangeForm,
    UserCreationForm,
    UserProfileCreationForm,
)
from ideas.forms import IdeaForm
from ideas.models import Idea

from .models import Enterprise, UserProfile


@login_required
def logout(request):
    auth.logout(request)
    return redirect("index")


def login(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
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

    try:
        user_profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        user_ideas = []
        user_investments = []
    else:
        user_ideas = user_profile.ideas.all()
        user_investments = user_profile.investments.all()

    return render(
        request,
        "accounts/profile.html",
        {"form": form, "user_ideas": user_ideas, "user_investments": user_investments},
    )


@login_required
def edit_profile(request):
    user_profile = request.user.userprofile
    try:
        enterprise = request.user.userprofile.enterprise
    except Enterprise.DoesNotExist:
        enterprise = None

    if request.method == "POST":
        user_form = UserChangeForm(request.POST, instance=request.user)
        user_profile_form = UserProfileCreationForm(
            request.POST,
            instance=user_profile,
        )
        enterprise_form = EnterpriseCreationForm(
            request.POST,
            instance=enterprise,
        )
        valid = user_form.is_valid() and user_profile_form.is_valid()
        if valid:
            role = (user_profile_form.cleaned_data.get("role") or
                    user_profile.role)
            if role == "entrepreneur":
                valid = valid and enterprise_form.is_valid()
            if valid:
                user_form.save()
                user_profile_form.save()
                if role == "entrepreneur":
                    enterprise = enterprise_form.save(commit=False)
                    enterprise.user_profile = user_profile
                    enterprise.save()
                return redirect("accounts:profile")
    else:
        user_form = UserChangeForm(instance=request.user)
        user_profile_form = UserProfileCreationForm(instance=user_profile)
        enterprise_form = EnterpriseCreationForm(instance=enterprise)

    return render(
        request,
        "accounts/edit_profile.html",
        {
            "user_form": user_form,
            "user_profile_form": user_profile_form,
            "enterprise_form": enterprise_form,
        },
    )
