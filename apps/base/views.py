from django.http import HttpResponse
# from django.shortcuts import render


def home(request):
    return HttpResponse('<html><body>Olá Django!</html></body>', content_type='text/html')
