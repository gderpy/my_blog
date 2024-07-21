from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.template.loader import render_to_string
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import AddPostForm
from .models import Article, Category

# Create your views here.

def index(request):

    articles = Article.objects.all()

    data = {
        "title": "Главная страница",
        "articles": articles,
        "cat_selected": 0,
    }
    return render(request, "main/index.html", context=data)


def write_article(request):
    if request.method == "POST":
        form = AddPostForm(request.POST)
        if form.is_valid():
            form.save()
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


def login(request):
    data = {
        "title": "Авторизация",
    }

    return render(request, "main/login.html", context=data)


def registration(request):
    return render(request, "main/registration.html")


def show_category(request, slug_name):
    data = {
        "title": f"Категория: {Category.objects.get(slug=slug_name).name}",
        "cat_selected": Category.objects.get(slug=slug_name).pk
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

