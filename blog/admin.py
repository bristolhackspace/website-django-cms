from django.contrib import admin
from .models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "publish_date", "author", "is_published")
    list_filter = ("is_published", "publish_date")
    search_fields = ("title", "subtitle", "intro_text", "author")
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = "publish_date"
