"""
URL configuration for hackspace_cms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from blog.views import BlogPostDetailView, BlogPostListView
from events.api_views import OpenDayDetailView
from hackspace_cms import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # Headless API for open day
    path("api/open-day/<slug:slug>/", OpenDayDetailView.as_view(), name="open-day-detail"),

    # Blog API
    path("api/blog/", BlogPostListView.as_view(), name="blog-list"),
    path("api/blog/<slug:slug>/", BlogPostDetailView.as_view(), name="blog-detail"),

    # (django CMS URLs would also go here if you use the full CMS page tree)
    path("", include("cms.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
