from django import forms
from .models import *


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


class SubjectSearchForm(forms.Form):
    subject = forms.ModelChoiceField(
        label='Cari Subyek',
        queryset=Subject.objects.all().order_by("subcat_id"),

        widget=forms.Select(attrs={
            'class': 'form-control select2',
        })
    )


class VervarSearchForm(forms.Form):
    subject = forms.ModelChoiceField(
        label='Cari Variabel Vertikal',
        queryset=Vervar.objects.all().order_by("group_ver_id"),

        widget=forms.Select(attrs={
            'class': 'form-control select2',
        })
    )


class TurthSearchForm(forms.Form):
    subject = forms.ModelChoiceField(
        label='Cari Periode Turunan',
        queryset=Turth.objects.all().order_by("group_turth_id"),

        widget=forms.Select(attrs={
            'class': 'form-control select2',
        })
    )


class PeriodSearchForm(forms.Form):
    subject = forms.ModelChoiceField(
        label='Cari Periode ',
        queryset=Period.objects.all(),

        widget=forms.Select(attrs={
            'class': 'form-control select2',
        })
    )


class UnitSearchForm(forms.Form):
    subject = forms.ModelChoiceField(
        label='Cari Unit',
        queryset=Unit.objects.all(),

        widget=forms.Select(attrs={
            'class': 'form-control select2',
        })
    )


class VariableSearchForm(forms.Form):
    subject = forms.ModelChoiceField(
        label='Cari Variabel',
        queryset=Variable.objects.all(),

        widget=forms.Select(attrs={
            'class': 'form-control select2',
        })
    )
