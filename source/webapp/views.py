from django.views.generic import ListView
from webapp.models import Photo


class IndexView(ListView):
    model = Photo
    template_name = 'index.html'
    context_key = 'photos'

