from django.contrib import admin, messages
from .models import Article, Category, LikedArticle


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "time_create", "category", "is_published", "brief_info")
    list_display_links = ("title", )
    ordering = ["-time_create", "title"]
    list_editable = ("is_published", )
    list_per_page = 5
    actions = ["set_published", "set_draft"]


    @admin.display(description="Объём контента", ordering="content")
    def brief_info(self, article: Article):
        return f"Содержит {len(article.content)} символов"
    

    @admin.action(description="Опубликовать выбранные статьи")    
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Article.Status.PUBLISHED)
        self.message_user(request, f"Изменено {count} записей.")

    
    @admin.action(description="Снять с публикации")
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Article.Status.DRAFT)
        self.message_user(request, f"Снято с публикации {count} записей.", messages.WARNING)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")


admin.site.register(LikedArticle)
