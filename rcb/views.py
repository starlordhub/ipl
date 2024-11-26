from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def rcb(request):
    return HttpResponse('<h1>captain of rcb</h1>Virat Kohli')