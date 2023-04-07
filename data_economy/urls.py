from django.urls import path, re_path
from .views import *

app_name = 'data'

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
]
