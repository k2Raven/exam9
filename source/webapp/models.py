from django.db import models
from django.contrib.auth.models import User


class Photo(models.Model):
    photo = models.ImageField(null=True, blank=True, upload_to='photo', verbose_name='Фотография')
    caption = models.CharField(max_length=300, verbose_name='Подпись')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата-время создания')
    likes = models.IntegerField(default=0, verbose_name='Лайки')
    author = models.ForeignKey(User, related_name='photo',
                               on_delete=models.CASCADE, verbose_name='Автор фотографии')

    def __str__(self):
        return self.caption


class Comments(models.Model):
    photo = models.ForeignKey('webapp.Photo', related_name='comments',
                              on_delete=models.CASCADE, verbose_name='Фотография')
    text = models.TextField(max_length=700, verbose_name='Комментарий')
    author = models.ForeignKey(User, related_name='comments',
                               on_delete=models.CASCADE, verbose_name='Автор комментария')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата-время создания')

    def __str__(self):
        return self.text


class Like(models.Model):
    photo = models.ForeignKey('webapp.Photo', related_name='like',
                              on_delete=models.CASCADE, verbose_name='Фотография')
    author = models.ForeignKey(User, related_name='like',
                               on_delete=models.CASCADE, verbose_name='Автор лайка')
