from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def mi(request):
    return HttpResponse('<h1>captain of mi</h1>Rohit sharma')