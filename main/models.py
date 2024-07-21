from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, db_index=True, unique=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)

    class Meta:
        ordering = ["-time_create"]
        indexes = [
            models.Index(fields=["-time_create"])
        ]

    def get_absolute_url(self):
        return reverse("show_article", kwargs={"article_id": self.pk})

    def __str__(self):
        return self.title






