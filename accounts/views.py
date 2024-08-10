from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout as auth_logout
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
from .models import UserProfile

from ideas.models import Idea

from django.forms import inlineformset_factory


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
            return redirect("accounts:profile")
    else:
        form = IdeaForm()

    user_ideas = request.user.userprofile.ideas.all()

    return render(
        request,
        "accounts/profile.html",
        {"form": form, "user_ideas": user_ideas},
    )


@login_required
def idea(request, idea_id):
    idea = get_object_or_404(Idea, pk=idea_id)
    return render(request, "accounts/idea.html", {"idea": idea})


@login_required
def aplicar(request):
    return render(request, "accounts/aplicou.html")
