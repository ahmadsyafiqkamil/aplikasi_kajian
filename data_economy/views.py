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
        page = request.POST.get('page')
        draw = int(request.POST.get('draw'))
        # start = int(request.POST.get('start'))
        # length = int(request.POST.get('length'))
        info = api.get_list(domain=domain, model="infographic", page=draw)
        print(info)
        return JsonResponse(info, safe=False)
    else:
        return HttpResponse("Invalid request method")


class PressReleaseView(LoginRequiredMixin, generic.TemplateView):
    template_name = "content/data/press.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = DomainSearchForm()
        return context


def get_press_release(request):
    if request.method == 'POST':
        api = API()
        domain = request.POST.get('domain')
        page = request.POST.get('page')
        draw = int(request.POST.get('draw'))
        # start = int(request.POST.get('start'))
        # length = int(request.POST.get('length'))
        data = api.get_list(domain=domain, model="pressrelease", page=draw)
        return JsonResponse(data, safe=False)
    else:
        return HttpResponse("Invalid request method")


def get_view_press(request):
    if request.method == "POST":
        id = request.POST.get('id')
        domain = request.POST.get('domain')
        api = API()
        data = api.get_view(id=id, domain=domain, model="pressrelease")
        return JsonResponse(data, safe=False)
    else:
        return HttpResponse("Invalid request method")


class SubjectView(LoginRequiredMixin, generic.TemplateView):
    template_name = "content/data/subject.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = DomainSearchForm()
        return context


def get_subject(request):
    if request.method == 'POST':
        api = API()
        domain = request.POST.get('domain')
        page = request.POST.get('page')
        draw = int(request.POST.get('draw'))
        # start = int(request.POST.get('start'))
        # length = int(request.POST.get('length'))
        info = api.get_list(domain=domain, model="subject", page=draw)
        print(info)
        return JsonResponse(info, safe=False)
    else:
        return HttpResponse("Invalid request method")


class DynamicData(LoginRequiredMixin, generic.TemplateView):
    template_name = "content/data/data_dinamis.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subject_form'] = SubjectSearchForm()
        context['domain_form'] = DomainSearchForm()
        return context


def get_data(request):
    if request.method == "POST":
        api = API()
        domain = request.POST.get('domain')
        subject = request.POST.get('subject')
        model = request.POST.get('model')

        match model:
            case "var":
                page = request.POST.get('page')
                # draw = int(request.POST.get('draw'))
                # start = int(request.POST.get('start'))
                # length = int(request.POST.get('length'))
                data = api.get_list(model=model, domain=domain, subject=subject, page=page)
                print(data)
                return JsonResponse(data, safe=False)

            case 'turth':
                page = request.POST.get('page')
                id_var = request.POST.get('id_var')
                # draw = int(request.POST.get('draw'))
                # start = int(request.POST.get('start'))
                # length = int(request.POST.get('length'))
                data = api.get_list(model=model, domain=domain, id_var=id_var, page=page)
                print(data)
                return JsonResponse(data, safe=False)

            case 'turvar':
                page = request.POST.get('page')
                id_var = request.POST.get('id_var')
                # draw = int(request.POST.get('draw'))
                # start = int(request.POST.get('start'))
                # length = int(request.POST.get('length'))
                data = api.get_list(model=model, domain=domain, id_var=id_var, page=page)
                print(data)
                return JsonResponse(data, safe=False)

            case "vervar":
                page = request.POST.get('page')
                id_var = request.POST.get('id_var')
                # draw = int(request.POST.get('draw'))
                # start = int(request.POST.get('start'))
                # length = int(request.POST.get('length'))
                data = api.get_list(model=model, domain=domain, page=page, id_var=id_var)
                print(data)
                return JsonResponse(data, safe=False)
    else:
        return HttpResponse("Invalid request method")
