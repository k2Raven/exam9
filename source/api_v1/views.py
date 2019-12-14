from rest_framework import viewsets
from webapp.models import Comments, Photo
from api_v1.serializers import CommentsSerializer, PhotoSerializer


class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

