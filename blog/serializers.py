from rest_framework import serializers
from django.conf import settings
from .models import BlogPost
from urllib.parse import urljoin

class BlogPostListSerializer(serializers.ModelSerializer):
    main_image_url = serializers.SerializerMethodField()
    class Meta:
        model = BlogPost
        fields = [
            "slug",
            "title",
            "subtitle",
            "intro_text",
            "main_image_url",
            "publish_date",
            "author",
        ]
    
    def get_main_image_url(self, obj):
        if not obj.main_image:
            return None
        return urljoin(settings.MEDIA_URL, obj.main_image.name)

class BlogPostDetailSerializer(serializers.ModelSerializer):
    main_image_url = serializers.SerializerMethodField()

    class Meta:
        model = BlogPost
        fields = [
            "slug",
            "title",
            "subtitle",
            "intro_text",
            "main_image_url",
            "body_html",
            "publish_date",
            "author",
        ]
    
    def get_main_image_url(self, obj):
        if not obj.main_image:
            return None
        return urljoin(settings.MEDIA_URL, obj.main_image.name)
