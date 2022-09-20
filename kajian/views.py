from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import KajianForm, ProgresKajianForm
from .models import Kajian, ProgresKajian


class HomeView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'home.html'
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    success_url = '/kajian_list/'


class KajianView(LoginRequiredMixin, generic.FormView):
    template_name = 'content/kajian.html'
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    form_class = KajianForm
    success_url = '/kajian_list/'

    # def get_form_kwargs(self):
    #     kwargs = {'user': self.request.user, }
    #     return kwargs

    def form_valid(self, form):
        kajian = form.save(commit=False)
        kajian.created_by = self.request.user
        kajian.save()
        form.save_m2m()
        return super(KajianView, self).form_valid(form)


class KajianListView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'content/kajian_list.html'


class KajianEditView(LoginRequiredMixin, generic.edit.UpdateView):
    model = Kajian
    template_name = 'content/kajian.html'
    form_class = KajianForm
    success_url = '/kajian_list/'

    def form_valid(self, form):
        kajian = form.save(commit=False)
        kajian.created_by = self.request.user
        kajian.save()
        form.save_m2m()
        return super(KajianEditView, self).form_valid(form)


class KajianDeleteView(LoginRequiredMixin, generic.edit.DeleteView):
    success_url = reverse_lazy("kajian:kajian_list")
    model = Kajian


class KajianDetailView(LoginRequiredMixin, generic.DetailView):
    model = Kajian
    template_name = 'content/kajian_detail.html'


class ProgressKajianTambah(LoginRequiredMixin, generic.edit.CreateView):
    model = ProgresKajian
    template_name = 'content/progres_kajian.html'
    form_class = ProgresKajianForm
    success_url = '/kajian_list/'

    def form_valid(self, form):
        print(self.kwargs["pk"])
        progres = form.save(commit=False)
        progres.kajian = Kajian.objects.get(id=self.kwargs["pk"])
        progres.save()
        return super(ProgressKajianTambah, self).form_valid(form)

