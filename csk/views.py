from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def csk(request):
    return HttpResponse('<h1>captain of csk</h1>Ruturaj Gaikwad')
