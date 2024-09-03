from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render, HttpResponse, HttpResponseRedirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.views.generic import CreateView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import LoginUserForm, RegisterUserForm, MainUserForm, AddUserForm
from .models import UserProfile


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = "users/login.html"
    extra_context = {
        "title": "Авторизация",
    }

    def get_success_url(self):
        return reverse_lazy("home")
    

class RegisterUser(CreateView):
    model = get_user_model()
    form_class = RegisterUserForm
    template_name = "users/registration.html"
    extra_context = {"title": "Регистрация"}
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data["password1"])
        user.save()

        UserProfile.objects.update_or_create(
            user=user,
            defaults={
                "sex": form.cleaned_data.get("sex", "Unknown"),
                "birthdate": form.cleaned_data.get("birthdate")
            }
        )

        return render(self.request, "users/register_done.html", {"user": user})
    
    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)
    

class UserProfileView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = "users/profile.html"
    context_object_name = "user"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_profile_exists = UserProfile.objects.filter(user=self.object).exists() # type: ignore
        if user_profile_exists:
            context["user_profile"] = UserProfile.objects.get(user=self.object) # type: ignore
        return context
    

class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User 
    form_class = MainUserForm
    template_name = "users/edit_profile.html"

    def get_success_url(self):
        return reverse_lazy("users:profile", kwargs={"pk": self.object.pk})

    def get_object(self, queryset=None):
        return self.request.user
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context["profile_form"] = AddUserForm(self.request.POST, instance=self.request.user.userprofile) # type: ignore
        else:
            context["profile_form"] = AddUserForm(instance=self.request.user.userprofile) # type: ignore
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        profile_form = context["profile_form"] # type: ignore
        if form.is_valid() and profile_form.is_valid():
            self.object = form.save()
            profile_form.save()
            return super().form_valid(form)
        else:
            return self.form_invalid(form)
        


        





