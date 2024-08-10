from django.urls import path, include

from .views import logout, profile, aplicar, idea


app_name = "accounts"

urlpatterns = [
    path("logout/", logout, name="logout"),
    path("profile/", profile, name="profile"),
    path("aplicar/", aplicar, name="aplicar"),
    path("<int:idea_id>/", idea, name="idea"),
]
