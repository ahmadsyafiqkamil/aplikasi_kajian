from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.serializers.json import DjangoJSONEncoder


class InfografisDatatable(View):
    def post(self, request):
        infografis = self._datatables(request)
        return JsonResponse(infografis)

    def _datatables(self, request):
        datatables = request.POST
        draw = int(datatables.get('draw'))
        # Ambil start
        start = int(datatables.get('start'))
        # Ambil length (limit)
        length = int(datatables.get('length'))


def infografis_list(request):
    data_context = {}
    return render(request, 'content/test.html', data_context)
