from django.urls import path, include

from .views import index, register, login, browse, filter_ideas

app_name = "dashboard"

urlpatterns = [
    path("", index, name="index"),
    path("register/", register, name="register"),
    path("login/", login, name="login"),
    path("browse/", browse, name="browse"),
    path("browse/filter_ideas", filter_ideas, name="filter_ideas"),
]
