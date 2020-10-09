from django.shortcuts import render


def video(request, slug):
    midias = {
        'motivacao': {'titulo': 'Luciano Ramalho OO em Python', 'youtube_id': 'BwAF7ke7Px0'},
        'instalacao-windows': {'titulo': 'Python Set Pratice - Conjuntos', 'youtube_id': 'euSpcIikBrw'}
    }

    midia = midias[slug]
    return render(request, 'aperitivo/video.html', context={'video': midia})
