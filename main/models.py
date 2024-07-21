from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, db_index=True, unique=True)

    def __str__(self):
        return self.name


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Article.Status.PUBLISHED)


class Article(models.Model):

    class Status(models.IntegerChoices):
        DRAFT = 0, "Черновик"
        PUBLISHED = 1, "Опубликовано"

    title = models.CharField(max_length=300)
    content = models.TextField()
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(choices=Status.choices, default=Status.DRAFT) # type: ignore
    category = models.ForeignKey("Category", on_delete=models.CASCADE)

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ["-time_create"]
        indexes = [
            models.Index(fields=["-time_create"])
        ]

    def get_absolute_url(self):
        return reverse("show_article", kwargs={"article_id": self.pk})

    def __str__(self):
        return self.title






