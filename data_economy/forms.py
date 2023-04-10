from django import forms
from .models import Domain


class DomainSearchForm(forms.Form):
    domain = forms.ModelChoiceField(
        label='Cari domain',
        queryset=Domain.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control select2',
        })
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        pass
