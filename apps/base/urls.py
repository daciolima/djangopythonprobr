from django.urls import path
from apps.base.views import home
urlpatterns = [
    path('', home)
]
