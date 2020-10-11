from django.shortcuts import render
from django.urls import reverse


class Video:
    def __init__(self, slug, titulo, youtube_id):
        self.slug = slug
        self.titulo = titulo
        self.youtube_id = youtube_id

    def get_absolute_url(self):
        return reverse('aperitivo:video', args=(self.slug, ))


midias = [
    Video('motivacao', 'Luciano Ramalho OO em Python', 'BwAF7ke7Px0'),
    Video('instalacao-windows', 'Python Set Pratice - Conjuntos', 'euSpcIikBrw')
    ]

videos_dct = {v.slug: v for v in midias}


def indice(request):
    return render(request, 'aperitivo/indice.html', context={'videos': midias})


class Video:
    def __init__(self, slug, titulo, youtube_id):
        self.slug = slug
        self.titulo = titulo
        self.youtube_id = youtube_id


midias = [
    Video('motivacao', 'Luciano Ramalho OO em Python', 'BwAF7ke7Px0'),
    Video('instalacao-windows', 'Python Set Pratice - Conjuntos', 'euSpcIikBrw')
    ]


def video(request, slug):
    midia = videos_dct[slug]
    return render(request, 'aperitivo/video.html', context={'video': midia})
