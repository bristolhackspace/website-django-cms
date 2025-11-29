from django.db import models

# Create your models here.
class OpenDay(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=200)

    # What you currently have in HTML:
    banner_text = models.TextField(
        help_text="Top banner message (e.g. ‘Sorry we have sold out!’)"
    )
    body_html = models.TextField(
        help_text="Main content in HTML (paragraphs, links, etc.)"
    )

    date = models.DateField(help_text="Date of the open day")
    entry_from = models.CharField(max_length=50, help_text="e.g. '11am'")
    last_entry = models.CharField(max_length=50, help_text="e.g. '4:30pm'")
    ticket_url = models.URLField()
    accessibility_note = models.TextField(blank=True)

    class Meta:
        verbose_name = "Open Day"
        verbose_name_plural = "Open Days"

    def __str__(self):
        return self.title