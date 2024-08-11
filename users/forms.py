from django import forms 


class LoginUserForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control my-4 py-2",
                                                             "placeholder": "Логин"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control my-4 py-2",
                                                                 "placeholder": "Пароль"}))
    