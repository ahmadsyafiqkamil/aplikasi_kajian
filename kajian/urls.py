from django.urls import path
from .views import *

app_name = 'kajian'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('kajian/', KajianView.as_view(), name='kajian'),
    # path('login/', LoginView.as_view(), name='login'),

]
