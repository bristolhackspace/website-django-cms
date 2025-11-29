from rest_framework import serializers
from .models import OpenDay

class OpenDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = OpenDay
        fields = [
            "slug",
            "title",
            "banner_text",
            "body_html",
            "date",
            "entry_from",
            "last_entry",
            "ticket_url",
            "accessibility_note",
        ]
