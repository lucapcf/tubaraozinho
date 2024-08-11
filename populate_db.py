import os
import django
from django.utils.crypto import get_random_string
import decimal

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from accounts.models import User, UserProfile, Enterprise
from ideas.models import Idea

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

def create_idea(user_profile, title, description, investment_value):
    idea = Idea.objects.create(
        user_profile=user_profile,
        title=title,
        description=description,
        investment_value=investment_value,
        return_on_investment=decimal.Decimal("0.00")
    )
    return idea

def populate():
    investors_info = [
        ("Alice", "Silva", "aliceinv"),
        ("Roberto", "Costa", "robertoinv"),
        ("Maria", "Fernandes", "mariainv")
    ]
    entrepreneurs_standard_info = [
        ("Carlos", "Machado", "carlosemp"),
        ("Joana", "Prado", "joanaemp"),
        ("Lucas", "Pereira", "lucasemp")
    ]
    entrepreneurs_premium_info = [
        ("Ana", "Ribeiro", "anaemp"),
        ("Felipe", "Santos", "felipeemp"),
        ("Clara", "Soares", "claraemp")
    ]

    # Criar investidores
    for first, last, username in investors_info:
        user = create_user(f"{username}", "123123", f"{username}@example.com", first, last)
        create_user_profile(user, "investor", cpf=get_random_string(length=11, allowed_chars="1234567890"))

    # Criar empreendedores standard
    for i, (first, last, username) in enumerate(entrepreneurs_standard_info, 1):
        user = create_user(f"{username}", "123123", f"{username}@example.com", first, last)
        profile = create_user_profile(
            user, "entrepreneur", cpf=get_random_string(length=11, allowed_chars="1234567890"), entrepreneur_tier="standard"
        )
        create_enterprise(profile, f"Startup Standard {i}", get_random_string(length=14, allowed_chars="1234567890"))

        ideas = [
            ("Plataforma de E-learning", "Plataforma interativa para cursos online com foco em tecnologia e negócios.", decimal.Decimal("20000.00")),
            ("App de Saúde Mental", "Aplicativo que oferece técnicas de mindfulness e acompanhamento psicológico online.", decimal.Decimal("15000.00")),
            ("Solução de Caronas Compartilhadas", "Sistema para otimizar o compartilhamento de caronas em áreas urbanas, reduzindo o tráfego e a poluição.", decimal.Decimal("25000.00"))
        ]

        for title, description, investment_value in ideas:
            create_idea(profile, title, description, investment_value)

    # Criar empreendedores premium
    for i, (first, last, username) in enumerate(entrepreneurs_premium_info, 1):
        user = create_user(f"{username}", "123123", f"{username}@example.com", first, last)
        profile = create_user_profile(
            user, "entrepreneur", cpf=get_random_string(length=11, allowed_chars="1234567890"), entrepreneur_tier="premium"
        )
        create_enterprise(profile, f"Startup Premium {i}", get_random_string(length=14, allowed_chars="1234567890"))

        ideas = [
            ("Plataforma de Inteligência Artificial", "Sistema avançado de AI para personalização de conteúdo em mídias sociais.", decimal.Decimal("50000.00")),
            ("Solução IoT para Agricultura", "Dispositivos IoT para monitoramento e análise de grandes culturas agrícolas, melhorando a eficiência e a produtividade.", decimal.Decimal("40000.00")),
            ("Sistema Blockchain para Logística", "Plataforma que utiliza blockchain para garantir a transparência e a segurança na cadeia de suprimentos.", decimal.Decimal("55000.00"))
        ]

        for title, description, investment_value in ideas:
            create_idea(profile, title, description, investment_value)

if __name__ == "__main__":
    populate()
