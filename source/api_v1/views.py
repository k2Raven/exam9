from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.response import Response
from webapp.models import Comments, Photo, Like
from api_v1.serializers import CommentsSerializer, PhotoSerializer, LikesSerializer


class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikesSerializer


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    @action(methods=['post'], detail=True)
    def like_up(self, request, pk=None):
        photo = self.get_object()
        photo.likes += 1
        photo.save()
        return Response({'id': photo.pk, 'rating': photo.likes})

    @action(methods=['post'], detail=True)
    def like_down(self, request, pk=None):
        photo = self.get_object()
        photo.likes -= 1
        photo.save()
        return Response({'id': photo.pk, 'rating': photo.likes})

