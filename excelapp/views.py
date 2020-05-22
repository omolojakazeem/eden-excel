import csv

from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render


# Create your views here.
from pandas import io


def about(request):
    return HttpResponse('<h1>Blog About hello hello</h1>')

def loading(request):
    template = 'loader.html'
    return render(request, template)

def contact(request):
    return HttpResponse('contant view')