from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
from django.utils.text import slugify

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

    # store HTML; editors can include <img>, <a>, iframe, etc.
    body_html = models.TextField(
        help_text="Full body (HTML). Can contain images, embeds, etc."
    )

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
        super().save(*args, **kwargs)
