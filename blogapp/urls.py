from django.urls import path

from .views import BlogListView, PostDetailView

app_name = "blogapp"

urlpatterns = [
    path("", BlogListView.as_view(), name="list-posts"),
    path("<post_slug>/", PostDetailView.as_view(), name="post-detail"),
]
