from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import (
    IdeaForm,
)
from .models import UserProfile

from ideas.models import Idea

from django.core.exceptions import PermissionDenied


from django.forms import inlineformset_factory


@login_required
def idea(request, idea_id):
    idea = get_object_or_404(Idea, pk=idea_id)
    return render(request, "ideas/idea.html", {"idea": idea})


@login_required
def create_idea(request):
    if request.method == "POST":
        form = IdeaForm(request.POST)
        if form.is_valid():
            idea = form.save(commit=False)
            idea.user_profile = request.user.user_profile
            idea.save()
            return redirect("ideas:idea", idea_id=idea.id)
    else:
        form = IdeaForm()
    return render(request, "ideas/create_idea.html", {"form": form})


@login_required
def edit_idea(request, idea_id):
    idea = get_object_or_404(Idea, pk=idea_id)
    if idea.user_profile.user != request.user:
        raise PermissionDenied()

    if request.method == "POST":
        form = IdeaForm(request.POST, instance=idea)
        if form.is_valid():
            form.save()
            return redirect("ideas:idea", idea_id=idea.id)
    else:
        form = IdeaForm(instance=idea)
    return render(request, "ideas/edit_idea.html", {"form": form, "idea": idea})
