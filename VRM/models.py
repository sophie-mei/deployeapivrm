from django.db import models

# Create your models here.

class Person(models.Model): 
    idPerson = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20) 
    birth_year = models.DateField(max_length=20) 
    adress = models.CharField(max_length=60) 

