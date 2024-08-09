import os
import django
from django.utils.crypto import get_random_string
from random import randint

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from accounts.models import User, UserProfile, Enterprise, Idea


def create_user(username, password, email, first, last):
    user = User.objects.create_user(
        username=username,
        password=password,
        email=email,
        first_name=first,
        last_name=last,
    )
    return user


def create_user_profile(user, role, cpf, entrepreneur_tier=None):
    profile = UserProfile.objects.create(
        user=user, role=role, cpf=cpf, entrepreneur_tier=entrepreneur_tier
    )
    return profile


def create_enterprise(user_profile, name, cnpj):
    enterprise = Enterprise.objects.create(
        user_profile=user_profile, name=name, cnpj=cnpj
    )
    return enterprise


def create_idea(user_profile, title, description):
    idea = Idea.objects.create(
        user_profile=user_profile, title=title, description=description
    )
    return idea


def populate():
    investors = [("Alice", "Johnson"), ("Bob", "Smith"), ("Carol", "Williams")]
    entrepreneurs_standard = [("David", "Brown"), ("Eve", "Davis"), ("Frank", "Miller")]
    entrepreneurs_premium = [("Grace", "Wilson"), ("Harry", "Moore"), ("Ivy", "Taylor")]

    for i, (first, last) in enumerate(investors, 1):
        user = create_user(
            f"investor{i}", "123123", f"investor{i}@example.com", first, last
        )
        create_user_profile(
            user,
            "investor",
            cpf=get_random_string(length=11, allowed_chars="1234567890"),
        )

    for i, (first, last) in enumerate(entrepreneurs_standard, 1):
        user = create_user(
            f"entrepreneur_standard{i}",
            "123123",
            f"entrepreneur_standard{i}@example.com",
            first,
            last,
        )
        profile = create_user_profile(
            user,
            "entrepreneur",
            cpf=get_random_string(length=11, allowed_chars="1234567890"),
            entrepreneur_tier="standard",
        )
        create_enterprise(
            profile,
            f"Enterprise Standard {i}",
            cnpj=get_random_string(length=14, allowed_chars="1234567890"),
        )

        for j in range(1, 4):
            create_idea(
                profile,
                f"Idea {j} of Standard Entrepreneur {i}",
                f"This is a description of idea {j} for Entrepreneur {i}.",
            )

    for i, (first, last) in enumerate(entrepreneurs_premium, 1):
        user = create_user(
            f"entrepreneur_premium{i}",
            "123123",
            f"entrepreneur_premium{i}@example.com",
            first,
            last,
        )
        profile = create_user_profile(
            user,
            "entrepreneur",
            cpf=get_random_string(length=11, allowed_chars="1234567890"),
            entrepreneur_tier="premium",
        )
        create_enterprise(
            profile,
            f"Enterprise Premium {i}",
            cnpj=get_random_string(length=14, allowed_chars="1234567890"),
        )

        for j in range(1, 4):
            create_idea(
                profile,
                f"Idea {j} of Premium Entrepreneur {i}",
                f"This is a description of idea {j} for Entrepreneur {i}.",
            )


if __name__ == "__main__":
    populate()
