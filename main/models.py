from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length=255, db_index=True, unique=True, verbose_name="Поле Slug")

    class Meta:
        verbose_name = "Категории"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("show_category", kwargs={"slug_name": self.slug})


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Article.Status.PUBLISHED)


class Article(models.Model):

    class Status(models.IntegerChoices):
        DRAFT = 0, "Черновик"
        PUBLISHED = 1, "Опубликовано"

    title = models.CharField(max_length=300, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание статьи")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата последнего обновления")
    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)), default=Status.DRAFT, verbose_name="Публикация") # type: ignore
    category = models.ForeignKey("Category", on_delete=models.PROTECT, related_name="articles", verbose_name="Категория")
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="articles")

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        verbose_name = "Статьи"
        verbose_name_plural = "Статьи"
        ordering = ["-time_create"]
        indexes = [
            models.Index(fields=["-time_create"])
        ]

    def get_absolute_url(self):
        return reverse("show_article", kwargs={"article_id": self.pk})

    def __str__(self):
        return self.title
    







