from typing import Any
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm 
from django.contrib.auth import get_user_model
from .models import UserProfile


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control my-4 py-2",
                                                             "placeholder": "Логин"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control my-4 py-2",
                                                                 "placeholder": "Пароль"}))

    class Meta:
        model = get_user_model()
        fields = ["username", "password"]


class RegisterUserForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(f"Password1 виджет: {self.fields['password1'].widget}")
        print(f"Password1 виджет: {self.fields['password2'].widget}")

    first_name = forms.CharField(
        max_length=50,
        required=True, 
        label="Имя",
        widget=forms.TextInput(attrs={"class": "form-control", "id": "inputFirstName"}))
    
    last_name = forms.CharField(
        max_length=50,
        required=True, 
        label="Фамилия",
        widget=forms.TextInput(attrs={"class": "form-control", "id": "inputLastName"}))
    
    email = forms.EmailField(
        required=True,
        label="E-mail",
        widget=forms.EmailInput(attrs={"class": "form-control", "id": "inputEmail4"})
    )

    sex = forms.ChoiceField(
        choices=UserProfile.SEX_CHOICES[0:2],
        required=False,
        label="Пол",
        widget=forms.RadioSelect(attrs={"class": "form-check-input"})
    )

    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={"class": "form-control", "id": "inputPassword4"})
    )

    password2 = forms.CharField(
        label="Подтвердите пароль",
        widget=forms.PasswordInput(attrs={"class": "form-control", "id": "confirmPassword4"})
    )

    birthdate = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'class': 'form-control', 'id': 'birthDate', 'type': 'date'}),
        label="Дата рождения"
    )

    username = forms.CharField(
        max_length=100,
        required=True,
        label="Ваш псевдоним",
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'inputNickname'})
    )
       
    class Meta:
        model = get_user_model()
        fields = ["first_name", "last_name", "email", "sex", "password1", "password2", "birthdate", "username"]


    def clean_email(self):
        email = self.cleaned_data["email"]
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Такой E-mail уже зарегистрирован")
        return email
    

class EditProfileUserForm(forms.ModelForm):
    
    # Поля из модели User
    username = forms.CharField(
        disabled=True, 
        label="Никнейм на сайте", 
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'inputNickname'}))

    class Meta:
        model = get_user_model()





    

    