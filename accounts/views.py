from django.shortcuts import render
from django.views import generic
from.form import CustomUserCreationForm
from .models import CustomUser

class SignUpView(generic.CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'


