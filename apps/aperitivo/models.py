from django.db import models
from django.urls import reverse


class Video(models.Model):

    titulo = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    youtube_id = models.CharField(max_length=20, unique=True)
    creation = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('aperitivo:video', args=(self.slug, ))

    def __str__(self):
        return f'Vídeos: {self.titulo}'
