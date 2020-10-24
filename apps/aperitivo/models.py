from django.db import models
from django.urls import reverse


class Video(models.Model):

    slug = models.CharField(max_length=50, unique=True)
    titulo = models.CharField(max_length=30, unique=True)
    youtube_id = models.CharField(max_length=20, unique=True)

    def get_absolute_url(self):
        return reverse('aperitivo:video', args=(self.slug, ))
