from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import BlogPost
from .serializers import BlogPostListSerializer, BlogPostDetailSerializer

# Create your views here.
class BlogPostListView(ListAPIView):
    serializer_class = BlogPostListSerializer

    def get_queryset(self):
        # Only published posts, newest first (ordering from model meta)
        return BlogPost.objects.filter(is_published=True)

class BlogPostDetailView(RetrieveAPIView):
    lookup_field = "slug"
    serializer_class = BlogPostDetailSerializer

    def get_queryset(self):
        return BlogPost.objects.filter(is_published=True)
