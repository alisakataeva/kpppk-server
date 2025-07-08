from django.shortcuts import render
from django.http import FileResponse, HttpResponse


# Create your views here.


def blank(request):
    if request.method == 'GET':
        return HttpResponse('<h1>Hello blank</h1>')
