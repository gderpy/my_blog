from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import CreateView
from .forms import LoginUserForm, RegisterUserForm


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = "users/login.html"
    extra_context = {
        "title": "Авторизация",
    }

    def get_success_url(self):
        return reverse_lazy("home")
    

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = "users/registration.html"
    extra_context = {"title": "Регистрация"}
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data["password1"])
        user.save()
        return render(self.request, "users/register_done.html", {"user": user})
    
    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)
    

# def register(request):
#     if request.method == "POST":
#         form = RegisterUserForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.set_password(form.cleaned_data["password1"])
#             user.save()
#             return render(request, "users/register_done.html")
#     else:      
#         form = RegisterUserForm()

#     data = {
#         "form": form,
#     }
    
#     return render(request, "users/registration.html", context=data)





