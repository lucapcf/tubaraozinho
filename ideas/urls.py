from django.urls import path, include

from .views import idea, create_idea, delete_idea, edit_idea


app_name = "ideas"

urlpatterns = [
    path("<int:idea_id>/", idea, name="idea"),
    path("create_idea/", create_idea, name="create_idea"),
    path("<int:idea_id>/edit/", edit_idea, name="edit_idea"),
    path("<int:idea_id>/delete/", delete_idea, name="delete_idea"),
]
