from django import forms
from django.contrib.auth.forms import (
    UserCreationForm as BaseUserCreationForm,
    UserChangeForm as BaseUserChangeForm,
    AuthenticationForm,
)
from .models import User, UserProfile, Enterprise
from ideas.models import Idea


class UserCreationForm(BaseUserCreationForm):
    class Meta(BaseUserCreationForm.Meta):
        model = User
        fields = BaseUserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "email",
        )


class UserChangeForm(BaseUserChangeForm):
    password = None

    class Meta(BaseUserChangeForm.Meta):
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
        )


class UserProfileCreationForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = (
            "cpf",
            "role",
            "entrepreneur_tier",
        )


class EnterpriseCreationForm(forms.ModelForm):
    class Meta:
        model = Enterprise
        fields = ("name", "cnpj")


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
