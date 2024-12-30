from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


from app.models import *

def insert_dept(requset):
    dname=input('enter dname: ')
    dno=int(input('enter dept no: '))
    loc=input('enter loc: ')
    
    DTO=Dept.objects.get_or_create(dept_name=dname,dept_no=dno,loc=loc)
    if DTO[1]:
        return HttpResponse('The New Department is created')
    else:
        return HttpResponse('Department already exists')


def insert_emp(requset):
    eno=int(input('enter emp no: '))
    ename=input('enter emp name: ')
    sal=int(input('enter salary: '))
    job=input('enter job: ')
    comm=input('enter comm: ')
    if comm:
        comm=int(comm)
    else:
        comm=None

    mgr=input('enter mgr no: ')
    if mgr:
        mgr=int(mgr)
        mgro=Emp.objects.get(emp_no=mgr)
    else:
        mgro=None
    
        

    dept_no=int(input('enter dept no: '))
    deptobj=Dept.objects.filter(dept_no=dept_no)
    
    
    
    ETO=Emp.objects.get_or_create(emp_no=eno,ename=ename,job=job,sal=sal,comm=comm,mgr=mgro,dept_no=deptobj[0])
