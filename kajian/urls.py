from django.urls import path
from .views import *
from .ajax_datatable import KajianAjaxView

app_name = 'kajian'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('kajian/', KajianView.as_view(), name='kajian'),
    path('kajian_list/', KajianListView.as_view(), name='kajian_list'),
    path('KajianAjaxView/', KajianAjaxView.as_view(), name='kajian_ajax_view'),
    # path('KajianDatatable/', KajianDatatable.as_view(), name='kajiandatatable'),
    # path('login/', LoginView.as_view(), name='login'),

]
