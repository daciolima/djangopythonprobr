from django.http import HttpResponse
# from django.shortcuts import render
from django.shortcuts import render


def home(request):
    return render(request, 'base/index.html')
