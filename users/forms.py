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


class RegisterUserForm(forms.ModelForm):
    first_name = forms.CharField(label="Имя", widget=forms.TextInput(attrs={"class": "form-control", "id": "inputFirstName"}))
    last_name = forms.CharField(label="Фамилия", widget=forms.TextInput(attrs={"class": "form-control", "id": "inputLastName"}))
    email = forms.EmailField(label="E-mail", widget=forms.EmailInput(attrs={"class": "form-control", "id": "inputEmail4"}))
    sex = forms.ChoiceField(label="Пол", choices=[("male", "Мужской"), ("female", "Женский")], widget=forms.RadioSelect(attrs={"class": "form-check-input", "name": "gender"}))
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'inputPassword4'}))
    password2 = forms.CharField(label="Подтвердите пароль", widget=forms.PasswordInput(attrs={"class": "form-control", "id": "confirmPassword"}))
    birthdate = forms.DateField(label="Дата рождения", widget=forms.DateInput(attrs={'class': 'form-control', 'id': 'birthDate', 'type': 'date'}))
    username = forms.CharField(label="Никнейм на сайте", widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'inputNickname'}))


    class Meta:
        model = get_user_model()
        fields = ["first_name", "last_name", "email", "sex", "password1", "password2", "birthdate", "username"]


    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password1"] != cd["password2"]:
            raise forms.ValidationError("Пароли не совпадают")
        return cd["password1"]
    

    def clean_email(self):
        email = self.cleaned_data["email"]
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Такой E-mail уже зарегистрирован")
        return email 
    

    