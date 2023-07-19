from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "first_name", "is_staff")
    list_display_links = ("id", "email")
    list_filter = ("is_staff", "created_at")
    search_fields = (
        "id",
        "email" "first_name",
        "last_name",
        "username",
    )
