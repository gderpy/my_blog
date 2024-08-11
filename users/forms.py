from django import forms
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import get_user_model


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control my-4 py-2",
                                                             "placeholder": "Логин"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control my-4 py-2",
                                                                 "placeholder": "Пароль"}))

    class Meta:
        model = get_user_model()
        fields = ["username", "password"]
    