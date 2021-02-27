from django import forms
from django.forms import ModelForm
from .models import *
from django.db import models
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email= models.EmailField()
    first_name = models.CharField()
    last_name = models.CharField()
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "first_name", "last_name"]



class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'