from django import forms
from ideas.models import Idea


class IdeaForm(forms.ModelForm):
    class Meta:
        model = Idea
        fields = ["title", "description"]
