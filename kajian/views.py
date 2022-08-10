from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.views import LoginView
from .forms import CustomLoginForm
from .models import Kajian


# Create your views here.


class HomeView(generic.TemplateView):
    template_name = 'home.html'


class LoginView(LoginRequiredMixin, generic.TemplateView):
    login_url = '/login/'
