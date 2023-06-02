from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name=models.CharField(max_length=100,null=True,blank=True)
    last_name=models.CharField(max_length=100,null=True,blank=True)
    email=models.EmailField()
    roll=models.PositiveIntegerField(unique=True)
