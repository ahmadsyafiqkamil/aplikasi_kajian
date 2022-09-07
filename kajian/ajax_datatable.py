from ajax_datatable.views import AjaxDatatableView
from django.core.exceptions import PermissionDenied

from .models import Kajian


class KajianAjaxView(AjaxDatatableView):
    model = Kajian
    title = 'Daftar Kajian'
    initial_order = [["name", "asc"], ]
    length_menu = [[10, 20, 50, 100, -1], [10, 20, 50, 100, 'all']]
    search_values_separator = '+'
    column_defs = [
        # AjaxDatatableView.render_row_tools_column_def(),
        {'name': 'id', 'visible': False},
        {'name': 'name', 'visible': True, 'title': "Nama Kajian"},
        {'name': 'pj_kajian', 'visible': True, 'title': 'Penanggung Jawab Kajian'},
        {'name': 'uraian_singkat', 'visible': True, 'title': 'Uraian Singkat'},
        {'name': 'abstrak', 'visible': True, 'title': 'Abstrak'},
        {'name': 'anggota', 'visible': True, 'title': 'Anggota Kajian', 'm2m_foreign_field': 'anggota__username'},
        {'name': 'edit', 'title': 'Edit', 'searchable': False, 'orderable': False, },
    ]

    def customize_row(self, row, obj):
        row['edit'] = """
            <a href="#" class="btn btn-info btn-edit"
               onclick="var id=this.closest('tr').id.substr(4); alert('Edit Kajian: ' + id); return false;">
               Edit
            </a>
        """

    def get_initial_queryset(self, request=None):
        if not request.user.is_authenticated:
            raise PermissionDenied
        qs = self.model.objects.filter(created_by=self.request.user)
        return qs

    # def prepare_results(self, request, qs):
    #     data = []
    #     for i in qs:
    #         anggota = []
    #         for a in i.anggota.all():
    #             anggota.append(a.User.name)
    #         anggota = " ".join(anggota)
    #         data.append([
    #             i.id,
    #             i.name,
    #             i.url,
    #             i.created,
    #             i.created_by,
    #             i.updated,
    #             i.updated_by,
    #             i.pj_kajian,
    #             i.uraian_singkat,
    #             i.abstrak,
    #             anggota
    #         ])
    #     return data
