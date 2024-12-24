from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def html(request):
    return HttpResponse('''
<h1>This is HTML Property</h1>
<img src="image.jpg" alt="Image Not Found">
''')