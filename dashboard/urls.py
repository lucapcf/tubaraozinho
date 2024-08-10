from django.urls import path, include

from .views import index, browse, filter_ideas

app_name = "dashboard"

urlpatterns = [
    path("", index, name="index"),
    path("browse/", browse, name="browse"),
    path("browse/filter_ideas", filter_ideas, name="filter_ideas"),
]
