# Generated by Django 5.0.7 on 2024-08-11 15:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_remove_category_parent'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-time_create'], 'verbose_name': 'Статьи', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категории', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='articles', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='articles', to='main.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(verbose_name='Содержание статьи'),
        ),
        migrations.AlterField(
            model_name='article',
            name='is_published',
            field=models.BooleanField(choices=[(False, 'Черновик'), (True, 'Опубликовано')], default=0, verbose_name='Публикация'), # type: ignore
        ),
        migrations.AlterField(
            model_name='article',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='article',
            name='time_update',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата последнего обновления'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=300, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(db_index=True, max_length=255, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=255, unique=True, verbose_name='Поле Slug'),
        ),
    ]
