from django.views.generic import ListView, DetailView
from webapp.models import Photo


class IndexView(ListView):
    template_name = 'index.html'
    model = Photo
    context_object_name = 'photos'


class PhotoView(DetailView):
    template_name = 'detail.html'
    model = Photo
    context_object_name = 'photo'
