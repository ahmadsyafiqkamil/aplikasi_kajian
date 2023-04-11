from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpResponse
from django.views import generic
from django.views import View
from .models import *
from .forms import *
from .api import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.

class HomeView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'content/data/data.html'


class InfografisView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'content/data/infografis.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = DomainSearchForm()
        return context


class BeritaView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'content/data/berita.html'


def get_infografis(request):
    if request.method == 'POST':
        api = API()
        domain = request.POST.get('domain')
        # page = request.POST.get('page')
        draw = int(request.POST.get('draw'))
        # start = int(request.POST.get('start'))
        # length = int(request.POST.get('length'))
        info = api.get_list(domain=domain, model="infographic", page=draw)
        print(info)
        return JsonResponse(info, safe=False)
    else:
        return HttpResponse("Invalid request method")


def get_list_data(request):
    pass

# class ListData(LoginRequiredMixin, generic.TemplateView):
#     template_name = "content/data/list.html"
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         subject = kwargs.get("sbj")
#
#         match subject:
#             case "infographic":
#                 columns = [
#                     {"data": "title"},
#                     {"data": "category"},
#                     {
#                         "data": "img",
#                         "render": "function (data, type, full, meta) { return '<img src=\"' + data + '\" height=\"50\"/>'; }"
#                     },
#                     {
#                         "data": "dl",
#                         "render": "function (data, type, full, meta) { return '<a href=\"' + data + '\">Download</a>'; }"
#                     }
#                 ]
#                 context['columns'] = columns
#                 context['form'] = DomainSearchForm()
#                 context["th"] = """
#                     <th>Judul</th>
#                     <th>Kategori</th>
#                     <th>Image</th>
#                     <th>Download Link</th>
#                 """
#                 context["datatable_url"] = "/data_get_infografis/"
#                 return context
