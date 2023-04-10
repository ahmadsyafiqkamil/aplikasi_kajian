from django.urls import path, re_path
from .views import *

app_name = 'data'

urlpatterns = [
    path('_home/', HomeView.as_view(), name='home'),
    path('_infografis/', InfografisView.as_view(), name='infografis'),
    path('_berita/', BeritaView.as_view(), name='berita'),
    path('_get_infografis/', get_infografis, name='get_infografis'),
    # path('_get_infografis/<int:page>', get_infografis, name='get_infografis'),

]
