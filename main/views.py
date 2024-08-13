from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
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
            return redirect("home")
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


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")


class TestPage(TemplateView):
    template_name = "main/test.html"

