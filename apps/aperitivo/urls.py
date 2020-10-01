from django.urls import path
from apps.aperitivo.views import video


app_name = 'aperitivo'
urlpatterns = [
    path('<slug:slug>', video, name='video')
]
