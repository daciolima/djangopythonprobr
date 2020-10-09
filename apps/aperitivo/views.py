from django.shortcuts import render


def video(request, slug):
    video = {
        'titulo': 'Video Aperitivo: Motivação',
        'youtube_id': 'BwAF7ke7Px0'
    }
    return render(request, 'aperitivo/video.html', context={'video': video})
