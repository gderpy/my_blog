from django.urls import path, re_path, register_converter
from . import views 


urlpatterns = [
    path("", views.index, name="home"),
    path("write_article/", views.write_article, name="article_writing"),
    path("about/", views.about, name="about"),
    path("login/", views.login, name="login"),
    path("registration/", views.registration, name="registration"),
]