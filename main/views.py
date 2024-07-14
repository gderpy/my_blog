from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.template.loader import render_to_string
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

# Create your views here.

def index(request):
    data = {
        "title": "Главная страница",
    }
    return render(request, "main/index.html", context=data)


def write_article(request):
    data = {
        "title": "Написать свою статью",
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


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")

