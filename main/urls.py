from django.urls import path, re_path, register_converter, include
from . import views 


urlpatterns = [
    path("", views.index, name="home"),
    path("write_article/", views.write_article, name="article_writing"),
    path("about/", views.about, name="about"),
    path("category/<slug:slug_name>/", views.show_category, name="show_category"),
    path("articles/<int:article_id>/", views.show_article, name="show_article"),
]