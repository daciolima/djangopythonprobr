from django.shortcuts import render, get_object_or_404

from apps.aperitivo.models import Video

midias = [
    Video(slug='motivacao', titulo='Luciano Ramalho OO em Python', youtube_id='BwAF7ke7Px0'),
    Video(slug='instalacao-windows', titulo='Python Set Pratice - Conjuntos', youtube_id='euSpcIikBrw')
    ]

videos_dct = {v.slug: v for v in midias}


def indice(request):
    return render(request, 'aperitivo/indice.html', context={'videos': midias})


def video(request, slug):
    video = get_object_or_404(Video, slug=slug)
    return render(request, 'aperitivo/video.html', context={'video': video})
