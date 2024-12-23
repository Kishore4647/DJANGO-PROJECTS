from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def oldcaptain(request):
    return HttpResponse(''' <h1> This is VIRAT </h1> ''')
def captain(request):
    return HttpResponse(''' <h1> This is FAF </h1> ''')