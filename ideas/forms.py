from django import forms
from .models import Idea


class IdeaForm(forms.ModelForm):
    class Meta:
        model = Idea
        fields = [
            "title",
            "investment_value",
            "elapsed_time",
            "return_on_investment",
            "description",
        ]
