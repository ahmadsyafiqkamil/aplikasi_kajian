from django.urls import path
from .views import *

app_name = 'kajian'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),

]
