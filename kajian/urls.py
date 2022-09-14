from django.urls import path, re_path
from .views import *
from .ajax_datatable import KajianAjaxView

app_name = 'kajian'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('kajian/', KajianView.as_view(), name='kajian'),
    re_path('kajian_edit/(?P<pk>[-\w]*)$', KajianEditView.as_view(), name='kajian_edit'),
    path('kajian_list/', KajianListView.as_view(), name='kajian_list'),
    path('KajianAjaxView/', KajianAjaxView.as_view(), name='kajian_ajax_view'),
    # path('KajianDatatable/', KajianDatatable.as_view(), name='kajiandatatable'),
    # path('login/', LoginView.as_view(), name='login'),

]
