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
        print(request.POST)
        api = API()
        domain = request.POST.get('domain')
        draw = int(request.POST.get('draw'))
        start = int(request.POST.get('start'))
        length = int(request.POST.get('length'))
        page = start // length + 1
        info = api.get_list(domain=domain, model="infographic", page=page)
        info.update({"draw": draw})
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
        draw = int(request.POST.get('draw'))
        start = int(request.POST.get('start'))
        length = int(request.POST.get('length'))
        page = start // length + 1
        data = api.get_list(domain=domain, model="pressrelease", page=page)
        data.update({"draw": draw})
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
        draw = int(request.POST.get('draw'))
        start = int(request.POST.get('start'))
        length = int(request.POST.get('length'))
        page = start // length + 1
        data = api.get_list(domain=domain, model="subject", page=page)
        data.update({"draw": draw})
        return JsonResponse(data, safe=False)
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

        draw = int(request.POST.get('draw'))
        start = int(request.POST.get('start'))
        length = int(request.POST.get('length'))
        page = start // length + 1

        match model:
            case "var":

                data = api.get_list(model=model, domain=domain, subject=subject, page=page)
                data.update({"draw": draw})
                return JsonResponse(data, safe=False)

            case 'turth':
                id_var = request.POST.get('id_var')

                data = api.get_list(model=model, domain=domain, id_var=id_var, page=page)
                data.update({"draw": draw})
                return JsonResponse(data, safe=False)

            case 'th':
                id_var = request.POST.get('id_var')
                data = api.get_list(model=model, domain=domain, id_var=id_var, page=page)
                data.update({"draw": draw})
                return JsonResponse(data, safe=False)

            case 'turvar':
                id_var = request.POST.get('id_var')
                data = api.get_list(model=model, domain=domain, id_var=id_var, page=page)
                data.update({"draw": draw})
                return JsonResponse(data, safe=False)

            case "vervar":
                id_var = request.POST.get('id_var')
                data = api.get_list(model=model, domain=domain, page=page, id_var=id_var)
                data.update({"draw": draw})
                return JsonResponse(data, safe=False)

            case 'data':
                domain = request.POST.get('domain')
                subject = request.POST.get('subject')
                var_id = request.POST.get('var_id')
                th_id = request.POST.get('th_id')
                turvar_id = request.POST.get('turvar_id')
                turth_id = request.POST.get('turth_id')
                vervar_id = request.POST.get('vervar_id')

                print(domain, subject, var_id, th_id, turvar_id)
                data = api.get_list(model=model, domain=domain, subject=subject, var_id=var_id, th_id=th_id,
                                    turvar_id=turvar_id, turth_id=turth_id, vervar_id=vervar_id)

                return JsonResponse(data, safe=False)

    else:
        return HttpResponse("Invalid request method")
