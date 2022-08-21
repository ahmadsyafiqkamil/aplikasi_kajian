from django.forms import ModelForm, TextInput
from .models import Kajian
from django.utils.translation import gettext_lazy as _


class KajianForm(ModelForm):
    class Meta:
        model = Kajian
        fields = ('nama_kajian',)
        labels = {
            'nama_kajian': _('Nama Kajian'),
        }
        widgets = {
            'nama_kajian': TextInput(attrs={'class': 'form-control', }),
        }

    # def __init__(self, *args, **kwargs):
    # super().__init__(*args, **kwargs)
    # user = kwargs.pop('user')
    # self.logged_user = user
    # self.fields['nama_kajian'].widget.attrs.update({
    #     'class': 'form-control'
    # })
