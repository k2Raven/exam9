from rest_framework import serializers
from webapp.models import Comments, Photo


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('pk', 'text')


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('pk', 'likes')


class LikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('pk', 'photo', 'author')