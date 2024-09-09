from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views 

app_name = "users"

urlpatterns = [
    path("login/", views.LoginUser.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", views.RegisterUser.as_view(), name="registration"),
    path("profile/<int:pk>", views.UserProfileView.as_view(), name="profile"),
    path("edit_profile/", views.UserProfileUpdateView.as_view(), name="edit_profile"),
    path("favorites/", views.show_favorites, name="show_favorites"),
]