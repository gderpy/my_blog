from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    SEX_CHOICES = [
        ("M", "Мужской"),
        ("F", "Женский"),
        ("Unknown", "Неизвестен")
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sex = models.CharField(max_length=10, choices=SEX_CHOICES, default="Unknown")
    birthdate = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username
