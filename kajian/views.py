from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import KajianForm, ProgresKajianForm, KomenKajianForm
from .models import Kajian, ProgresKajian, KomenProgresKajian


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

    def form_valid(self, form):
        print(self.kwargs["pk"])
        progres = form.save(commit=False)
        progres.kajian = Kajian.objects.get(id=self.kwargs["pk"])
        progres.save()
        return super(ProgressKajianTambah, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('kajian:kajian_detail', kwargs={'pk': self.kwargs['pk']})


class ProgressKajianEdit(LoginRequiredMixin, generic.edit.UpdateView):
    model = ProgresKajian
    template_name = 'content/progres_kajian.html'
    form_class = ProgresKajianForm

    def get_success_url(self):
        pk = ProgresKajian.objects.values("kajian__id").get(id=self.kwargs["pk"])
        return reverse_lazy('kajian:kajian_detail',
                            kwargs={'pk': pk["kajian__id"]})


class ProgresKajianDelete(LoginRequiredMixin, generic.edit.DeleteView):
    model = ProgresKajian

    def get_success_url(self):
        pk = ProgresKajian.objects.values("kajian__id").get(id=self.kwargs["pk"])
        return reverse_lazy('kajian:kajian_detail',
                            kwargs={'pk': pk["kajian__id"]})


class TambahKomentarKajian(LoginRequiredMixin, generic.edit.CreateView):
    model = KomenProgresKajian
    template_name = 'content/progres_kajian.html'
    form_class = KomenKajianForm
    success_url = reverse_lazy('kajian:kajian_list')

    def form_valid(self, form):
        # print(self.model.progres.kajian.objects.get(id=self.kwargs["pk"]))
        progres = form.save(commit=False)
        progres.progres = ProgresKajian.objects.get(id=self.kwargs["pk"])
        progres.save()
        return super(TambahKomentarKajian, self).form_valid(form)

    # def get_success_url(self):
    #     return reverse_lazy('kajian:kajian_detail', kwargs={'pk': self.kwargs['pk']})

class ProgresDetail(LoginRequiredMixin,generic.DetailView):
    model = ProgresKajian
    template_name = 'content/detail_progress.html'

