from django.shortcuts import render, get_object_or_404

from apps.aperitivo.models import Video


def indice(request):
    videos = Video.objects.order_by('creation').all()

    return render(request, 'aperitivo/indice.html', context={'videos': videos})


def video(request, slug):
    video = get_object_or_404(Video, slug=slug)
    return render(request, 'aperitivo/video.html', context={'video': video})
