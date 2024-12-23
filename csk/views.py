from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def oldcaptaincsk(request):
    return HttpResponse('''<h1> This is MS DHONI </h1> ''')
def captaincsk(request):
    return HttpResponse('''<h1> This is RUTU </h1>  ''')