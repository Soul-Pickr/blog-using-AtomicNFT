from django.db import models

# Create your models here.

class content(models.Model):
    title= models.CharField(max_length=500)
    topic= models.CharField(max_length=1000)
    des= models.CharField(max_length=5000)
    