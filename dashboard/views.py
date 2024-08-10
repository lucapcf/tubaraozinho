from django.shortcuts import render, redirect
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


@login_required
def browse(request):
    ideas = Idea.objects.all()
    return render(request, "dashboard/browse.html", {"ideas": ideas})


@login_required
def filter_ideas(request):
    query = request.GET.get("title", "")
    ideas = Idea.objects.filter(title__icontains=query)
    return render(request, "dashboard/browse.html", {"ideas": ideas})
