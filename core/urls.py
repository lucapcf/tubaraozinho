from django.contrib import admin
from django.urls import path, include
from dashboard.views import index


urlpatterns = [
    path("", index, name="index"),
    path("dashboard/", include("dashboard.urls", namespace="dashboard")),
    path("accounts/", include("accounts.urls", namespace="accounts")),
    path("ideas/", include("ideas.urls", namespace="ideas")),
    path("admin/", admin.site.urls),
]
