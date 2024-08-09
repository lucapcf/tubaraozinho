from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import (
    LoginForm,
    UserProfileCreationForm,
    UserCreationForm,
    EnterpriseCreationForm,
    IdeaForm,
)
from .models import Idea, UserProfile

from django.forms import inlineformset_factory


def index(request):
    featured_ideas = Idea.objects.all().order_by("-created_at")[:5]
    context = {"featured_ideas": featured_ideas}

    return render(request, "accounts/index.html", context)


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
                request, user, backend="django.contrib.auth.backends.ModelBackend"
            )
            return redirect("profile")

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
def logout(request):
    auth_logout(request)
    return redirect("index")


@login_required
def profile(request):
    if request.method == "POST":
        form = IdeaForm(request.POST)
        if form.is_valid():
            idea = form.save(commit=False)
            idea.user_profile = request.user.userprofile
            idea.save()
            return redirect("profile")
    else:
        form = IdeaForm()

    user_ideas = request.user.userprofile.ideas.all()

    return render(
        request, "accounts/profile.html", {"form": form, "user_ideas": user_ideas}
    )


@login_required
def browse(request):
    ideas = Idea.objects.all()
    return render(request, "accounts/browse.html", {"ideas": ideas})


@login_required
def filter_ideas(request):
    query = request.GET.get("title", "")
    ideas = Idea.objects.filter(title__icontains=query)
    return render(request, "accounts/browse.html", {"ideas": ideas})


@login_required
def idea(request, idea_id):
    idea = get_object_or_404(Idea, pk=idea_id)
    return render(request, "browse/idea.html", {"idea": idea})
