from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import (
    IdeaForm,
)
from .models import UserProfile

from ideas.models import Idea

from django.forms import inlineformset_factory


@login_required
def idea(request, idea_id):
    idea = get_object_or_404(Idea, pk=idea_id)
    return render(request, "ideas/idea.html", {"idea": idea})
