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
    path('_analisis_data/', AnalisisDataView.as_view(), name='analisis_data'),
    path('_get_infografis/', get_infografis, name='get_infografis'),
    path('_get_press/', get_press_release, name='get_press'),
    path('_get_view_press/', get_view_press, name='get_view_press'),
    path('_get_subject/', get_subject, name='get_subject'),
    path('_get_data/', get_data, name='get_data'),
    path('_download/', download_file, name='download'),
    path('_save/', simpan_data, name='simpan'),
    path('_get_data_home/', get_data_home, name='get_data_home'),
    path('_get_data_pd/', get_data_pd, name='get_data_pd'),
    path('_get_column/', get_column, name='get_column'),
    path('_get_predict/', get_predict, name='data_get_predict'),
    path('_download_data/', download_data, name='_download_data'),
    path('_example/', example, name='example'),

    # path('_list_data/<str:sbj>', ListData.as_view(), name='ListData'),
]
