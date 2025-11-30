from rest_framework import serializers
from .models import BlogPost

class BlogPostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = [
            "slug",
            "title",
            "subtitle",
            "intro_text",
            "main_image",
            "publish_date",
            "author",
        ]

class BlogPostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = [
            "slug",
            "title",
            "subtitle",
            "intro_text",
            "main_image",
            "body_html",
            "publish_date",
            "author",
        ]
