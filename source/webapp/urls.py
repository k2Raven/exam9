from django.urls import path
from webapp.views import IndexView, PhotoView, PhotoCreateView, PhotoUpdateView

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('photo/<int:pk>/', PhotoView.as_view(), name='detail_photo'),
    path('photo/create/', PhotoCreateView.as_view(), name='photo_create'),
    path('photo/update/<int:pk>/', PhotoUpdateView.as_view(), name='photo_update'),
]