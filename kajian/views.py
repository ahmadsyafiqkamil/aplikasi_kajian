from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.views import LoginView
from .forms import KajianForm
from .models import Kajian


# Create your views here.


class HomeView(generic.TemplateView):
    template_name = 'home.html'


class KajianView(LoginRequiredMixin, generic.FormView):
    template_name = 'content/kajian.html'
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    form_class = KajianForm
    success_url = '/kajian/'

    # def get_form_kwargs(self):
    #     kwargs = {'user': self.request.user, }
    #     return kwargs

    def form_valid(self, form):
        kajian = form.save(commit=False)
        kajian.created_by = self.request.user
        kajian.save()
        print(self.get_success_url())
        return super(KajianView, self).form_valid(form)

