from django.urls import path

from .views import index, register, login, logout, profile, browse, filter_ideas, idea, aplicar


urlpatterns = [
    path("", index, name="index"),
    path("register/", register, name="register"),
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("profile/", profile, name="profile"),
    path("browse/", browse, name="browse"),
    path("browse/filter_ideas", filter_ideas, name="filter_ideas"),
    path("browse/<int:idea_id>/", idea, name="idea"),
    path('aplicar/', aplicar, name='aplicar'),
]
