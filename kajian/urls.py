from django.urls import path, re_path
from .views import *
from .ajax_datatable import KajianAjaxView

app_name = 'kajian'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('kajian/', KajianView.as_view(), name='kajian'),
    path('kajian_list/', KajianListView.as_view(), name='kajian_list'),
    path('KajianAjaxView/', KajianAjaxView.as_view(), name='kajian_ajax_view'),
    re_path('kajian_edit/(?P<pk>[-\w]*)$', KajianEditView.as_view(), name='kajian_edit'),
    re_path('kajian_delete/(?P<pk>[-\w]*)$', KajianDeleteView.as_view(), name='kajian_delete'),
    re_path('kajian_detail/(?P<pk>[-\w]*)$', KajianDetailView.as_view(), name='kajian_detail'),
    re_path('kajian_tambah_progress/(?P<pk>[-\w]*)$', ProgressKajianTambah.as_view(), name='kajian_tambah_progres'),
    # re_path('progres_kajian_list/(?P<pk>[-\w]*)$', ProgressKajianDetailView.as_view(), name='progress_kajian_list'),

    # path('KajianDatatable/', KajianDatatable.as_view(), name='kajiandatatable'),
    # path('login/', LoginView.as_view(), name='login'),

]
