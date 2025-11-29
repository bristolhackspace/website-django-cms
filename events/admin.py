from django.contrib import admin
from .models import OpenDay

# Register models here.
@admin.register(OpenDay)
class OpenDayAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "date")
    prepopulated_fields = {"slug": ("title",)}