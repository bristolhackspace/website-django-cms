import json
from django.contrib import admin
from django.utils.html import format_html
from .models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ("body_json_pretty",)

    fieldsets = (
        (None, {"fields": ("title", "slug", "subtitle", "intro_text", "main_image")}),
        ("Content", {"fields": ("body_html", "body_json_pretty")}),
        ("Publishing", {"fields": ("author", "publish_date", "is_published")}),
    )

    def body_json_pretty(self, obj: BlogPost) -> str:
        return format_html("<pre>{}</pre>", json.dumps(obj.body_json, indent=2, sort_keys=True))

    body_json_pretty.short_description = "Derived JSON"

