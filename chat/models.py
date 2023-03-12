from django.db import models
from datetime import datetime
from pickle import TRUE

# Create your models here.
class Room(models.Model):
    name = models.IntegerField(default=0)
    

class Message(models.Model):
    value= models.CharField(max_length=100000)
    date= models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=100)
    room = models.CharField(max_length=100)
    