from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class state(models.Model):
    title = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='pics')


class Image(models.Model):
    title = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='pics')
    state = models.CharField(max_length=40 , default="no state", blank = True , null=True)

class Hotels(models.Model):
    name = models.CharField(max_length=20 , blank=True , null=True)
    phone_number = models.CharField(max_length=10 , blank=True , null=True)
    photo = models.ImageField(upload_to='pics', blank=True , null=True)
    state = models.CharField(max_length=20, blank=True , null=True)
    near_by = models.CharField(max_length=20, blank=True , null=True)
    price = models.CharField(max_length=20, blank=True , null=True)
    

    
class Booking(models.Model):
    name = models.CharField(max_length=20 , blank=True , null=True)
    phone_number = models.CharField(max_length=10 , blank=True , null=True)
    number_of_peoples = models.IntegerField( blank=True , null=True)
    number_of_rooms = models.IntegerField( blank=True , null=True)
    check_in_date = models.DateTimeField(blank=True , null=True)
    chekout_out_date = models.DateTimeField(blank=True , null=True)
    amount = models.IntegerField(default = 0 , blank = True , null=True)
