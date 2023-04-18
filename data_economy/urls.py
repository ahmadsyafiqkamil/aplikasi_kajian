from django.urls import path, re_path
from .views import *

app_name = 'data'

urlpatterns = [
    path('_home/', HomeView.as_view(), name='home'),
    path('_infografis/', InfografisView.as_view(), name='infografis'),
    path('_press/', PressReleaseView.as_view(), name='press'),
    path('_dynamic_data/', DynamicData.as_view(), name='dynamic_data'),
    path('_subject/', SubjectView.as_view(), name='subject'),
    path('_berita/', BeritaView.as_view(), name='berita'),
    path('_get_infografis/', get_infografis, name='get_infografis'),
    path('_get_press/', get_press_release, name='get_press'),
    path('_get_view_press/', get_view_press, name='get_view_press'),
    path('_get_subject/', get_subject, name='get_subject'),
    path('_get_data/', get_data, name='get_data'),
    path('_download/', download_file, name='download'),
    path('_save/', simpan_data, name='simpan'),

    # path('_list_data/<str:sbj>', ListData.as_view(), name='ListData'),
]
