from django.contrib import admin

from apps.application.models import Application


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "user")
    list_display_links = ("title",)
