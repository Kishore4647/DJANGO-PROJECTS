from django.db import models

# Create your models here.


class Dept(models.Model):
    dept_name=models.CharField(max_length=100)
    dept_no=models.IntegerField(primary_key=True)
    loc=models.CharField(max_length=100)

class Emp(models.Model):
    emp_no=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    sal=models.DecimalField(max_digits=10,decimal_places=3,null=True,blank=True)
    comm=models.DecimalField(max_digits=10,decimal_places=3,null=True,blank=True)
    dept_no=models.ForeignKey(Dept,on_delete=models.CASCADE)
    mgr=models.ForeignKey('self',on_delete=models.SET_NULL,null=True,blank=True)
    


 