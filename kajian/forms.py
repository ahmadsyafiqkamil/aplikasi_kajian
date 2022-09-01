# from django.forms import ModelForm, TextInput
from django import forms
from .models import Kajian
from django.utils.translation import gettext_lazy as _
from django.forms import modelformset_factory


# KajianFormSet = modelformset_factory(
#     Kajian,
#     fields=('nama_kajian',),
#     labels={
#         'nama_kajian': _('Nama Kajian'),
#     },
#     widgets={
#         'nama_kajian': TextInput(attrs={'class': 'form-control', }),
#     }, extra=1,
# )

class KajianForm(forms.ModelForm):
    class Meta:
        model = Kajian
        fields = ('nama_kajian', 'pj_kajian', 'anggota')
        labels = {
            'nama_kajian': _('Nama Kajian'),
            'pj_kajian': _('Penanggung Jawab'),
            'anggota': _('Nama Anggota'),
        }
        widgets = {
            'nama_kajian': forms.TextInput(attrs={'class': 'form-control', }),
            'pj_kajian': forms.Select(attrs={'class': 'form-control select2', }),
            'anggota': forms.SelectMultiple(attrs={'class': 'form-control select2', 'multiple': 'multiple'}),
        }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     user = kwargs.pop('user')
    #     self.logged_user = user
    #     self.fields['nama_kajian'].widget.attrs.update({
    #         'class': 'form-control'
    #     })
