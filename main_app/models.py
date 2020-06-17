from django.db import models

# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=50)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()