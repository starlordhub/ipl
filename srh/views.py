from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def srh(request):
    return HttpResponse('<h1>captain of srh</h1>Pat Cummins')