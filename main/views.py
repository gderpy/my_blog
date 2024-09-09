from django.http import HttpResponseNotFound, HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import AddPostForm
from .models import Article, Category

# Create your views here.

def index(request):

    articles = Article.published.all()


    data = {
        "title": "Главная страница",
        "articles": articles,
        "cat_selected": 0,
    }
    return render(request, "main/index.html", context=data)


@login_required
def write_article(request):
    if request.method == "POST":
        form = AddPostForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return render(request, "main/article_moderation.html")
    else:
        form = AddPostForm()

    data = {
        "title": "Написать свою статью",
        "form": form,
    }

    return render(request, "main/write_article.html", context=data)


def about(request):
    return render(request, "main/about.html")


def show_category(request, slug_name):
    category = get_object_or_404(Category, slug=slug_name)
    articles = Article.published.filter(category_id=category.pk)

    data = {
        "title": f"Категория: {category.name}",
        "articles": articles,
        "cat_selected": category.pk
    }
    return render(request, "main/index.html", context=data)


def show_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)

    data = {
        "title": article.title,
        "article": article,
    }

    return render(request, "main/article.html", context=data)


def toggle_article_action(request, article_id, action_type):
    article = get_object_or_404(Article, pk=article_id)

    if action_type == "like":
        queryset = article.likes
        template = "main/snippets/likes.html"
    elif action_type == "favorite":
        queryset = article.favorites
        template = "main/snippets/favorites.html"
    else:
        return JsonResponse({"error": "Неверное действие"}, status=400)
    
    user_exist = queryset.filter(username=request.user.username).exists()

    if user_exist:
        queryset.remove(request.user)
    else:
        queryset.add(request.user)

    data = {
        "article": article,
        "action_type": action_type
    }

    return render(request, template, context=data)


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")



