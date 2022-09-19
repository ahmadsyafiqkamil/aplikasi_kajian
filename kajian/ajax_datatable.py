from ajax_datatable.views import AjaxDatatableView
from django.core.exceptions import PermissionDenied
from django.utils.translation import gettext_lazy as _

from .models import Kajian


class KajianAjaxView(AjaxDatatableView):
    model = Kajian
    code = 'kajian'
    title = 'Daftar Kajian'
    initial_order = [["name", "asc"], ]
    length_menu = [[10, 20, 50, 100, -1], [10, 20, 50, 100, 'all']]
    search_values_separator = '+'
    column_defs = [
        # AjaxDatatableView.render_row_tools_coValueError: The 'file' attribute has no file associated with it.lumn_def(),
        {'name': 'id', 'visible': False},
        {'name': 'name', 'visible': True, 'title': "Nama Kajian"},
        {'name': 'pj_kajian', 'visible': True, 'title': 'Penanggung Jawab Kajian'},
        {'name': 'uraian_singkat', 'visible': True, 'title': 'Uraian Singkat'},
        {'name': 'abstrak', 'visible': True, 'title': 'Abstrak'},
        {'name': 'anggota', 'visible': True, 'title': 'Anggota Kajian', 'm2m_foreign_field': 'anggota__username'},
        {'name': 'file', 'visible': True, 'title': 'Dokumen', },
        # {'name': 'document', 'visible': True, 'title': 'Dokumen', },
        {'name': 'action', 'title': 'Aksi', 'searchable': False, 'orderable': False, },
    ]

    def customize_row(self, row, obj):
        file = self.model.objects.get(id=row["pk"])
        print(row["pk"])
        if file.file:
            path_file = file.file.url
        else:
            path_file = "#"
        row['file'] = """
        <a href="%s">file</a>
        """ % path_file
        row['action'] = f"""
                    <a href="#" class="btn btn-primary" id="add" 
                    onclick="add('{row['pk']}'); " >
                       Tambah Progress
                    </a>
                    <a href="#" class="btn btn-info btn-edit" id="edit"
                    onclick="edit('{row['pk']}'); " >
                       Edit
                    </a>
                    <a href="/kajian_delete/{row['pk']}" class="btn btn-danger" data-toggle="modal"
                    data-target="#delete-item-modal"
                    id="delete-item"
                    >
                    Delete
                    </a>
                """

    def get_initial_queryset(self, request=None):
        if not request.user.is_authenticated:
            raise PermissionDenied
        qs = self.model.objects.filter(created_by=self.request.user)
        return qs
