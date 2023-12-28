from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context

def index(request):
    return render(request, 'index.html')

def login(request):
    return HttpResponse('hola login 1111')

