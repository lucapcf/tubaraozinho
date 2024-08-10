from django.urls import path, include

from .views import register, login, logout, profile, edit_profile, aplicar, idea


app_name = "accounts"

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("profile/", profile, name="profile"),
    path("aplicar/", aplicar, name="aplicar"),
    path("<int:idea_id>/", idea, name="idea"),
    path("edit-profile/", edit_profile, name="edit_profile"),
]
