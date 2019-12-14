from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from webapp.models import Photo
from webapp.forms import PhotoForm

from django.urls import reverse_lazy


class IndexView(ListView):
    template_name = 'index.html'
    model = Photo
    context_object_name = 'photos'


class PhotoView(DetailView):
    template_name = 'detail.html'
    model = Photo
    context_object_name = 'photo'


class PhotoCreateView(LoginRequiredMixin, CreateView):
    template_name = 'create.html'
    model = Photo
    form_class = PhotoForm
    success_url = reverse_lazy('webapp:index')

    def form_valid(self, form):
        self.object = self.model.objects.create(author=self.request.user, **form.cleaned_data)
        return redirect(self.get_success_url())


class PhotoUpdateView(UpdateView):
    template_name = 'update.html'
    model = Photo
    form_class = PhotoForm
    success_url = reverse_lazy('webapp:index')

