from django.shortcuts import render

# Create your views here.
d={'name':'sreerag','age':20}

def conditions(request):
   
    return render(request,'conditions.html',context=d)

def ifelif(request):
    return render(request,'ifelif.html',d)
