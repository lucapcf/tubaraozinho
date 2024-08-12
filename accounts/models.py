from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.core.exceptions import ValidationError


class User(AbstractUser):
    email = models.EmailField(unique=True)


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
        self.clean()
        super().save(*args, **kwargs)

    def clean(self):
        if self.role == "investor" and self.entrepreneur_tier:
            raise ValidationError(
                {
                    "entrepreneur_tier": "Investors cannot have an entrepreneur tier"
                }
            )

    def __str__(self):
        return self.user.username


class Enterprise(models.Model):
    user_profile = models.OneToOneField(
        UserProfile,
        on_delete=models.CASCADE,
        related_name="enterprise"
    )
    name = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=14, unique=True)

    def __str__(self):
        return self.name
