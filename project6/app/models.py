from django.db import models

# Create your models here.

class Country(models.Model):
    country_name=models.CharField(max_length=100,primary_key=True)
    country_no=models.IntegerField()
    country_pm=models.CharField(max_length=100)


class Capital(models.Model):
    Capital_name=models.CharField(max_length=100)
    country_name=models.ForeignKey(Country,on_delete=models.CASCADE)
