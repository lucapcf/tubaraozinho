# Generated by Django 5.0.7 on 2024-08-11 21:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Idea",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                (
                    "investment_value",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("elapsed_time", models.IntegerField(default=0)),
                (
                    "return_on_investment",
                    models.DecimalField(decimal_places=2, max_digits=5),
                ),
                ("description", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "user_profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ideas",
                        to="accounts.userprofile",
                    ),
                ),
            ],
        ),
    ]
