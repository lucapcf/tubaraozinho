from django.shortcuts import render, redirect
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
    EnterpriseCreationForm,
)
from ideas.forms import (
    IdeaForm,
)
from accounts.models import UserProfile
from ideas.models import Idea

from django.forms import inlineformset_factory


def index(request):
    featured_ideas = Idea.objects.all().order_by("-created_at")[:5]
    context = {"featured_ideas": featured_ideas}

    return render(request, "dashboard/index.html", context)


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
    return render(request, "dashboard/login.html", {"form": form})


def register(request):
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        user_profile_form = UserProfileCreationForm(request.POST)
        enterprise_form = None

        valid = user_form.is_valid() and user_profile_form.is_valid()
        if valid:
            role = user_profile_form.cleaned_data.get("role")
            if role == "entrepreneur":
                enterprise_form = EnterpriseCreationForm(request.POST)
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
        "dashboard/register.html",
        {
            "user_form": user_form,
            "user_profile_form": user_profile_form,
            "enterprise_form": enterprise_form,
        },
    )


@login_required
def browse(request):
    ideas = Idea.objects.all()
    return render(request, "dashboard/browse.html", {"ideas": ideas})


@login_required
def filter_ideas(request):
    query = request.GET.get("title", "")
    ideas = Idea.objects.filter(title__icontains=query)
    return render(request, "dashboard/browse.html", {"ideas": ideas})
