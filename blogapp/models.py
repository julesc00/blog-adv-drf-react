import uuid

from django.db import models
from django.utils import timezone

from category.models import Category


def blog_directory_path(instance, filename):
    return f"blog/{instance}/{filename}"


class Post(models.Model):

    class PostObjects(models.Manager):
        """
        This will allow to show or not show a post without deleting it.
        """
        def get_queryset(self):
            return super().get_queryset().filter(status="published")

    options = (
        ("draft", "Draft"),
        ("published", "Published")
    )

    blog_uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    thumbnail = models.ImageField(upload_to=blog_directory_path)
    video = models.FileField(upload_to=blog_directory_path, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    excerpt = models.CharField(max_length=100)
    # author = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    published = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=options, default="draft")

    objects = models.Manager()  # default manager
    post_objects = PostObjects()  # custom manager

    class Meta:
        ordering = ("-published",)

    def __str__(self):
        return self.title

    def get_video(self):
        if self.video:
            return self.video.url
        return ""

    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        return ""

