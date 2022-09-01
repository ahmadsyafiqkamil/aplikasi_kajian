from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.views import LoginView
from .forms import KajianForm
from .models import Kajian
from django.urls import reverse_lazy
from django.shortcuts import redirect
from ajax_datatable.views import AjaxDatatableView
from django.contrib.auth.models import Permission


# Create your views here.


class HomeView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'home.html'
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    success_url = '/kajian_list/'


class KajianView(LoginRequiredMixin, generic.FormView):
    template_name = 'content/kajian.html'
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    form_class = KajianForm
    success_url = '/kajian_list/'

    # def get_form_kwargs(self):
    #     kwargs = {'user': self.request.user, }
    #     return kwargs

    def form_valid(self, form):
        kajian = form.save(commit=False)
        kajian.created_by = self.request.user
        kajian.save()
        return super(KajianView, self).form_valid(form)


class KajianListView(generic.ListView,AjaxDatatableView):
    model = Kajian
    template_name = 'content/kajian_list.html'
    title = 'Daftar Kajian'
    initial_order = [["app_label", "asc"], ]
    length_menu = [[10, 20, 50, 100, -1], [10, 20, 50, 100, 'all']]
    search_values_separator = '+'

    column_defs = [
        AjaxDatatableView.render_row_tools_column_def(),
        {'name': 'id', 'visible': False, },
        {'name': 'nama_kajian', 'visible': True, },
        {'name': 'pj_kajian', 'visible': True, },
        # {'name': 'app_label', 'foreign_field': 'content_type__app_label', 'visible': True, },
        # {'name': 'model', 'foreign_field': 'content_type__model', 'visible': True, },
    ]

    def get_queryset(self):
        return Kajian.objects.filter(created_by=self.request.user)

# class KajianView(generic.TemplateView):
#     template_name = 'content/kajian.html'
#
#     def get(self, *args, **kwargs):
#         formset = KajianFormSet(queryset=Kajian.objects.none())
#         return self.render_to_response({'form': formset})
#
#     def post(self, *args, **kwargs):
#         formset = KajianFormSet(data=self.request.POST)
#
#         if formset.is_valid():
#             formset.save()
#             return redirect(reverse_lazy('kajian:kajian_list'))
#
#         return self.render_to_response({'form': formset})



class PermissionAjaxDatatableView(AjaxDatatableView):

    model = Permission
    title = 'Permissions'
    initial_order = [["app_label", "asc"], ]
    length_menu = [[10, 20, 50, 100, -1], [10, 20, 50, 100, 'all']]
    search_values_separator = '+'

    column_defs = [
        AjaxDatatableView.render_row_tools_column_def(),
        {'name': 'id', 'visible': False, },
        {'name': 'codename', 'visible': True, },
        {'name': 'name', 'visible': True, },
        {'name': 'app_label', 'foreign_field': 'content_type__app_label', 'visible': True, },
        {'name': 'model', 'foreign_field': 'content_type__model', 'visible': True, },
    ]