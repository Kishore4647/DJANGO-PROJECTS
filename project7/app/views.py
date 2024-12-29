from django.shortcuts import render

# Create your views here.

from app.models import *

def insert_dept(request):
    dname=input('enter dname: ')
    dno=input('enter dept no: ')
    loc=input('enter location: ')
    