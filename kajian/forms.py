# from django.forms import ModelForm, TextInput
from django import forms
from .models import Kajian
from django.utils.translation import gettext_lazy as _
from django.forms import modelformset_factory


class KajianForm(forms.ModelForm):
    class Meta:
        model = Kajian
        fields = ('name', 'pj_kajian', 'anggota', 'uraian_singkat', 'abstrak', 'file')
        labels = {
            'name': _('Nama Kajian'),
            'pj_kajian': _('Penanggung Jawab'),
            'anggota': _('Nama Anggota'),
            'uraian_singkat': _('Uraian Singkat Kajian'),
            'abstrak': _('Abstrak'),
            'file': _('Dokumen'),
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', }),
            'pj_kajian': forms.Select(attrs={'class': 'form-control select2', }),
            'anggota': forms.SelectMultiple(attrs={'class': 'form-control select2', 'multiple': 'multiple'}),
            'uraian_singkat': forms.TextInput(attrs={'class': 'form-control', }),
            'abstrak': forms.Textarea(attrs={'class': 'form-control', }),
            'file': forms.FileInput(),
        }
