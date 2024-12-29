from django.db import models

# Create your models here.

class Dept(models.Model):
    dept_name=models.CharField(max_length=100)
    dept_no=models.IntegerField(primary_key=True)
    loc=models.CharField(max_length=100)

    #its wrong go to project 8-->>

class Emp(models.Model):
    dept_no=models.ForeignKey(Dept,on_delete=models.CASCADE)
    ename=models.CharField(max_length=100)
    emp_no=models.IntegerField()
    job=models.CharField(max_length=100)
    mgr=models.CharField(max_length=100)
    hire_date=models.DateField()
    salary=models.IntegerField()
    comm=models.DecimalField(decimal_places=3,max_digits=4)

class Salgrade(models.Model):
    grade=models.IntegerField()
    losal=models.IntegerField()
    hisal=models.IntegerField()


