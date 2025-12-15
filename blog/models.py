from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
from django.utils.text import slugify
from blog.content import html_to_blocks
from django_prose_editor.fields import ProseEditorField


class BlogPost(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300, blank=True)
    intro_text = models.TextField(help_text="Short intro/standfirst")

    # main image (can be optional)
    main_image = models.ImageField(
        upload_to="blog_main_images/",
        blank=True,
        null=True,
        help_text="Main image for the article",
    )

    body_html = ProseEditorField(
        extensions={
            # Keep this conservative to start; you can add more later.
            "Bold": True,
            "Italic": True,
            "Underline": True,
            "Strike": True,
            "HardBreak": True,
            "BulletList": True,
            "OrderedList": True,
            "ListItem": True,
            "Blockquote": True,
            "Heading": {"levels": [2, 3, 4]},
            "Link": {"protocols": ["http", "https", "mailto"]},
            "Image": {
                "inline": False,
                "allowBase64": False,  # keep this False for security/perf
            },
        },
        sanitize=True,
        help_text="Body content (rich text).",
    )

    # Derived, machine-friendly representation
    body_json = models.JSONField(default=dict, editable=False)


    author = models.CharField(max_length=100, help_text="Display name of the author")

    publish_date = models.DateField()
    is_published = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-publish_date", "-created_at"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        # Generate derived JSON from sanitized HTML
        self.body_json = html_to_blocks(self.body_html)
        
        super().save(*args, **kwargs)


class BlogImage(models.Model):
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to="blog_body_images/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title or self.image.name
