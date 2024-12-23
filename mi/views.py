from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def oldcaptainmi(request):
    return HttpResponse(''' <h1> This is ROHIT </h1> ''')
def captainmi(request):
    return HttpResponse(''' <h1> This is PANDIYA </h1>''')
