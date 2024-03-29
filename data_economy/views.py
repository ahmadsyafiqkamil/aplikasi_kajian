import os
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views import generic
from .forms import *
from django.utils.text import slugify
from .api import API
from .serializers import *
import json
from .tools import *
import logging


# Create your views here.
# pd.options.plotting.backend = "plotly"

def example(request):
    return render(request, 'example.html')


class HomeView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'content/data/data.html'


def get_data_home(request):
    aktifitas = AktifitasData.objects.all()
    serializer = AktifitasDataSerializer(aktifitas, many=True)
    data = {
        'data': serializer.data
    }
    return JsonResponse(data)


def get_data_pd(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        data = AktifitasData.objects.get(pk=id)
        # data_data = json.loads(data.data_data)
        data_dict = json.loads(data.data)

        df_reset = json_to_pd(data_dict)



        plot = plot_view(df_reset)
        context = {
            'html': df_reset.to_html(),
            'label': data.label_var,
            # "img": chart_url,
            "plot": plot
        }

        return JsonResponse(context, safe=False)


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


class AnalisisDataView(LoginRequiredMixin, generic.TemplateView):
    template_name = "content/data/analisis.html"


def get_column(request):
    if request.method == "POST":
        id = request.POST.get('id')
        data = AktifitasData.objects.get(id=id)
        data_dict = json.loads(data.data)
        # df_reset = json_to_pd(data_dict)
        data_data = data.data_data

        data_kolom = {
            # "var": data_data["tahun"],
            "tahun": data_data["tahun"],
            "turvar": data_data["turvar"],
            "vervar": data_data["vervar"],
            "turtahun": data_data["turtahun"],
        }

        return JsonResponse({'kolom': data_kolom}, safe=False)


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
                if data:
                    label = data["var"][0]["label"]
                    df = api.data_dinamis_transform_to_pd(data)

                    return JsonResponse({'html': df.to_html(), 'label': label}, safe=False)
                else:
                    return JsonResponse({'html': "html", 'label': "label"}, safe=False)

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
        print(dt)

        # Set the filename and Content-Disposition header
        filename = f'{slugify("Dataframe Pandas")}.csv'
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="{filename}"'

        # Write dataframe to response
        dt.to_csv(path_or_buf=response, index=True, encoding='utf-8')
        print(response.items())
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
        # json_data = dt.to_json()

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
            data=dt.to_json(),
            label_var=label,
            # data_data=data_data
            data_data=data_data
        )
        aktifitas.save()
        return JsonResponse({'hasil': "data tersimpan", 'label': label}, safe=False)


def download_data(request):
    if request.method == "POST":
        id = request.POST.get('id')
        data = AktifitasData.objects.get(id=id)
        data_dict = json.loads(data.data)
        df = json_to_pd(data_dict)
        print(df)

        filename = f'{slugify("Dataframe Pandas")}.csv'
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="{filename}"'

        # Write dataframe to response
        df.to_csv(path_or_buf=response, index=True, encoding='utf-8')
        print(response.items())

        return response


def get_predict(request):
    if request.method == "POST":
        id_data = request.POST.get('id')
        # checkboxes = request.POST.getlist('checkboxes')

        data = AktifitasData.objects.get(id=id_data)
        data_dict = json.loads(data.data)
        df = json_to_pd(data_dict)
        # print(df)
        tahun = request.POST.get('tahun')
        bulan = request.POST.get('bulan')
        vervar = request.POST.get('vervar')
        karakteristik = request.POST.get('karakteristik')

        filters = []

        if tahun != "0":
            filters.append(df['tahun'] == tahun)

        if bulan != "0":
            filters.append(df['bulan'] == bulan)

        if vervar != "0":
            filters.append(df['vervar'] == vervar)

        if karakteristik != "0":
            filters.append(df['karakteristik'] == karakteristik)

        if filters:
            data_filtered = df[pd.concat(filters, axis=1).all(axis=1)]
        else:
            data_filtered = df


        data_prediksi = predict(data_filtered)
        # print(data_prediksi)
        # print(data_filtered)
        # plot = plot_view(data_filtered)

        plot = plot_predict(data_prediksi)

        context = {
            "tabel": data_prediksi.to_html(),
            "plot": plot
        }

        return JsonResponse(context, safe=False)
