from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.models import Photo, Comments
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

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['Comments'] = Comments.objects.all()
        return context


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


class PhotoDeleteView(DeleteView):
    template_name = 'delete.html'
    model = Photo
    context_object_name = 'photo'
    success_url = reverse_lazy('webapp:index')