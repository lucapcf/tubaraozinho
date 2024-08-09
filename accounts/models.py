from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class User(AbstractUser):
    pass


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    ROLE_CHOICES = (
        ("entrepreneur", "Entrepreneur"),
        ("investor", "Investor"),
    )
    role = models.CharField(max_length=12, choices=ROLE_CHOICES)

    ENTREPRENEUR_TIER_CHOICES = (
        ("standard", "Standard"),
        ("premium", "Premium"),
    )
    entrepreneur_tier = models.CharField(
        max_length=8, choices=ENTREPRENEUR_TIER_CHOICES, blank=True, null=True
    )

    cpf = models.CharField(max_length=11, unique=True)

    def save(self, *args, **kwargs):
        if self.role == "investor":
            if self.entrepreneur_tier:
                self.entrepreneur_tier = None
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username


class Enterprise(models.Model):
    user_profile = models.OneToOneField(
        UserProfile,
        on_delete=models.CASCADE,
        related_name="enterprise",
        null=True,
        blank=True,
    )
    name = models.CharField(max_length=255, null=True, blank=True)
    cnpj = models.CharField(max_length=14, unique=True, null=True, blank=True)

    def __str__(self):
        return self.name


class Idea(models.Model):
    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name="ideas"
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
