from django.db import models
from accounts.models import UserProfile


class Idea(models.Model):
    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name="ideas"
    )
    title = models.CharField(max_length=200)
    investment_value = models.DecimalField(max_digits=10, decimal_places=2)
    elapsed_time = models.IntegerField(default=0)
    return_on_investment = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
