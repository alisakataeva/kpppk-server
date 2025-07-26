from django.shortcuts import render
from django.http import FileResponse, HttpResponse
from django.template import loader


# Create your views here.


def blank(request):
    if request.method == 'GET':
        return HttpResponse('<h1>Hello blank</h1>')


def index(request):
    if request.method == 'GET':
        template = loader.get_template("index.html")
        return HttpResponse(template.render({}, request))
