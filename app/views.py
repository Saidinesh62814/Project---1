from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dinesh(request):
    return HttpResponse('<h1> he is a kid </h1>')