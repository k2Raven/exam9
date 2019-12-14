from django import forms
from webapp.models import Photo


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ['created_at', 'author', 'likes', 'author']