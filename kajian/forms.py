# from django.forms import ModelForm, TextInput
from django import forms

from aplikasi_kajian import settings
from .models import Kajian, ProgresKajian, KomenProgresKajian
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.forms import modelformset_factory
from django.core.exceptions import ValidationError


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

    def clean_file(self):
        file = self.cleaned_data['file']
        if file:
            file_extension = file.name.split('.')[-1].lower()
            if file_extension not in settings.ALLOWED_DOCUMENT_EXTENSIONS:
                raise ValidationError(_('File yang diupload harus berupa dokumen (doc, docx, pdf, txt).'))
        return file

    def __init__(self, *args, **kwargs):
        super(KajianForm, self).__init__(*args, **kwargs)
        self.fields['pj_kajian'].queryset = User.objects.exclude(username="admin")
        self.fields['anggota'].queryset = User.objects.exclude(username="admin")


class ProgresKajianForm(forms.ModelForm):
    class Meta:
        model = ProgresKajian
        fields = ('name', 'progres','file')
        labels = {
            'name': _('Judul Progress'),
            'progres': _('Uraian Progres'),
            'file': _('Dokumen'),
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', }),
            'progres': forms.Textarea(attrs={'class': 'form-control', }),
            'file': forms.FileInput(),
        }

class KomenKajianForm(forms.ModelForm):
    class Meta:
        model = KomenProgresKajian
        fields = ('name', 'komentar','file')
        labels = {
            'name': _('Judul Komentar'),
            'komentar': _('Uraian Komentar'),
            'file': _('Dokumen'),
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', }),
            'komentar': forms.Textarea(attrs={'class': 'form-control', }),
            'file': forms.FileInput(),
        }
