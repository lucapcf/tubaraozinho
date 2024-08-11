from django.db import models
from django.contrib.auth.models import User

from ideas.models import Idea

from accounts.models import UserProfile

class Investment(models.Model):
    investor = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name="investments"
    )

    STATUS_CHOICES = [
        ('aprovada', 'Aprovada'),
        ('pendente', 'Pendente'),
        ('rejeitada', 'Rejeitada'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pendente')
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE, related_name="investments", null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_invested = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.investor.username} invested {self.amount} in {self.idea.title}"