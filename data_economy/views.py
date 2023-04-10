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
    template_name = 'content/data.html'


class InfografisView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'content/infografis.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = DomainSearchForm()
        return context


class BeritaView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'content/berita.html'


def get_infografis(request):
    if request.method == 'POST':
        api = API()
        domain = request.POST.get('domain')
        # page = request.POST.get('page')
        draw = int(request.POST.get('draw'))
        # start = int(request.POST.get('start'))
        # length = int(request.POST.get('length'))
        info = api.get_list(domain=domain, model="infographic", page=draw)
        return JsonResponse(info, safe=False)
    else:
        return HttpResponse("Invalid request method")
