from django.shortcuts import render, HttpResponse

# Create your views here.

def login_user(request):
    return HttpResponse("Авторизация")


def logout_user(request):
    return HttpResponse("Выход из профиля")
