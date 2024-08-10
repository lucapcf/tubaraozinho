from django.urls import path, include

from .views import idea


app_name = "ideas"

urlpatterns = [
    path("<int:idea_id>/", idea, name="idea"),
]
