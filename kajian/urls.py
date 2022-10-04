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
    re_path('kajian_detail_progress/(?P<pk>[-\w]*)$', ProgresDetail.as_view(), name='kajian_detail_progres'),
    re_path('kajian_edit_progress/(?P<pk>[-\w]*)$', ProgressKajianEdit.as_view(), name='kajian_edit_progres'),
    re_path('kajian_delete_progress/(?P<pk>[-\w]*)$', ProgresKajianDelete.as_view(), name='kajian_delete_progres'),
    re_path('komen_kajian/(?P<pk>[-\w]*)$', TambahKomentarKajian.as_view(), name='komen_kajian'),

    path('notifications/', NotificationListView.as_view(), name='notifications'),
    re_path('mark-as-read/(?P<slug>\d+)/$', mark_as_read, name='mark_as_read'),
]
