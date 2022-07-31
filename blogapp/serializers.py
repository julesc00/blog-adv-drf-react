from rest_framework import serializers

from .models import Post
from category.serializers import CategorySerializer


class PostSerializer(serializers.ModelSerializer):
    thumbnail = serializers.CharField(source="get_thumbnail")  # get from Post.get_thumbnail()
    video = serializers.CharField(source="get_video")
    category = CategorySerializer()

    class Meta:
        fields = (
            "blog_uuid",
            "title",
            "slug",
            "thumbnail",
            "video",
            "description",
            "excerpt",
            "category",
            "published",
            "status",
        )
