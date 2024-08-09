from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# from django.utils.translation import gettext_lazy as _

from .models import User, UserProfile, Idea, Enterprise


class UserProfileInline(admin.StackedInline):
    model = UserProfile


class EnterpriseAdmin(admin.ModelAdmin):
    list_display = ("name", "cnpj", "user_profile")
    search_fields = ("name", "cnpj", "user_profile__user__username")
    ordering = ("name",)


class UserAdmin(BaseUserAdmin):
    inlines = [UserProfileInline]


admin.site.register(User, UserAdmin)
admin.site.register(Idea)
admin.site.register(Enterprise, EnterpriseAdmin)
