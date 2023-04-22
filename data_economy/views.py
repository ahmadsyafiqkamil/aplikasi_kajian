from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpResponse
from django.views import generic
from .forms import *
import pandas as pd
from django.utils.text import slugify
from django.http import JsonResponse
from .api import API
from .models import *
from django.contrib.auth.models import User
from .serializers import *
from rest_framework import serializers
import json


# Create your views here.

class HomeView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'content/data/data.html'


def get_data_home(request):
    aktifitas = AktifitasData.objects.all()
    serializer = AktifitasDataSerializer(aktifitas, many=True)
    data = {
        'data': serializer.data
    }
    return JsonResponse({'data': serializer.data})


def get_data_pd(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        data = AktifitasData.objects.get(pk=id)
        data_dict = json.loads(data.data)
        data_tuples = []

        # Iterate through each key in data_dict and convert to tuple
        for key, value in data_dict['data'].items():
            # Remove brackets and quotes from key string, and split on comma
            key_parts = key.replace('\'', '').replace('(', '').replace(')', '').split(',')
            # Convert each part of key to a tuple
            index = tuple([x.strip() for x in key_parts])
            data_tuples.append(index + (value,))

        # Create pandas DataFrame with multi-index
        # "tahun", "bulan", "vervar", "karakteristik", "data_key"
        df = pd.DataFrame(data_tuples, columns=['tahun', 'bulan', 'vervar', 'karakteristik', 'data_key', 'Data'])
        df = df.set_index(['tahun', 'bulan', 'vervar', 'karakteristik', 'data_key'])

        return JsonResponse({'html': df.to_html(), 'label': data.label_var}, safe=False)


class BeritaView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'content/data/berita.html'


class InfografisView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'content/data/infografis.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = DomainSearchForm()
        return context


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

        match model:
            case "var":
                draw = int(request.POST.get('draw'))
                start = int(request.POST.get('start'))
                length = int(request.POST.get('length'))
                page = start // length + 1

                data = api.get_list(model=model, domain=domain, subject=subject, page=page)
                data.update({"draw": draw})
                return JsonResponse(data, safe=False)

            case 'turth':
                id_var = request.POST.get('id_var')
                draw = int(request.POST.get('draw'))
                start = int(request.POST.get('start'))
                length = int(request.POST.get('length'))
                page = start // length + 1

                data = api.get_list(model=model, domain=domain, id_var=id_var, page=page)
                data.update({"draw": draw})
                return JsonResponse(data, safe=False)

            case 'th':
                id_var = request.POST.get('id_var')
                draw = int(request.POST.get('draw'))
                start = int(request.POST.get('start'))
                length = int(request.POST.get('length'))
                page = start // length + 1
                data = api.get_list(model=model, domain=domain, id_var=id_var, page=page)
                data.update({"draw": draw})
                return JsonResponse(data, safe=False)

            case 'turvar':
                id_var = request.POST.get('id_var')
                draw = int(request.POST.get('draw'))
                start = int(request.POST.get('start'))
                length = int(request.POST.get('length'))
                page = start // length + 1
                data = api.get_list(model=model, domain=domain, id_var=id_var, page=page)
                data.update({"draw": draw})
                return JsonResponse(data, safe=False)

            case "vervar":
                id_var = request.POST.get('id_var')
                draw = int(request.POST.get('draw'))
                start = int(request.POST.get('start'))
                length = int(request.POST.get('length'))
                page = start // length + 1
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

                print(
                    f"domain: {domain}, subject: {subject}, var_id: {var_id}, th_id: {th_id}, turvar_id: {turvar_id}, turth_id: {turth_id}, vervar_id: {vervar_id}")
                data = api.get_list(model=model, domain=domain, subject=subject, var_id=var_id, th_id=th_id,
                                    turvar_id=turvar_id, turth_id=turth_id, vervar_id=vervar_id)
                label = data["var"][0]["label"]
                df = api.data_dinamis_transform_to_pd(data)

                return JsonResponse({'html': df.to_html(), 'label': label}, safe=False)

    else:
        return HttpResponse("Invalid request method")


def download_file(request):
    if request.method == "POST":
        api = API()
        model = request.POST.get('model')
        domain = request.POST.get('domain')
        subject = request.POST.get('subject')
        var_id = request.POST.get('var_id')
        th_id = request.POST.get('th_id')
        turvar_id = request.POST.get('turvar_id')
        turth_id = request.POST.get('turth_id')
        vervar_id = request.POST.get('vervar_id')

        data = api.get_list(model=model, domain=domain, subject=subject, var_id=var_id, th_id=th_id,
                            turvar_id=turvar_id, turth_id=turth_id, vervar_id=vervar_id)

        dt = api.data_dinamis_transform_to_pd(data)

        # Set the filename and Content-Disposition header
        filename = f'{slugify("Dataframe Pandas")}.csv'
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="{filename}"'

        # Write dataframe to response
        dt.to_csv(path_or_buf=response, index=True, encoding='utf-8')

        return response


def simpan_data(request):
    if request.method == "POST":
        api = API()
        model = request.POST.get('model')
        domain = request.POST.get('domain')
        subject = request.POST.get('subject')
        var_id = request.POST.get('var_id')
        th_id = request.POST.get('th_id')
        turvar_id = request.POST.get('turvar_id')
        turth_id = request.POST.get('turth_id')
        vervar_id = request.POST.get('vervar_id')

        data = api.get_list(model=model, domain=domain, subject=subject, var_id=var_id, th_id=th_id,
                            turvar_id=turvar_id, turth_id=turth_id, vervar_id=vervar_id)

        dt = api.data_dinamis_transform_to_pd(data)
        label = data["var"][0]["label"]
        json_data = dt.to_json()

        data_data = {
            "var": data["var"],
            "turvar": data["turvar"],
            "labelvervar": data["labelvervar"],
            "vervar": data["vervar"],
            "tahun": data["tahun"],
            "turtahun": data["turtahun"],
            "metadata": data["metadata"],
            "datacontent": data["datacontent"]
        }

        aktifitas = AktifitasData(
            user=request.user,
            data=json_data,
            label_var=label,
            data_data=data_data
        )
        aktifitas.save()
        return JsonResponse({'hasil': "data tersimpan", 'label': label}, safe=False)
