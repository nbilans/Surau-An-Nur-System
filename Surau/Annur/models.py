from django.test import TestCase

# Create your tests here.

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

#Create user profile model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    date_modified = models.DateTimeField(User, auto_now=True)

    def __str__(self):
        return self.user.username

#Create Profile When New User Signs Up
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
    
post_save.connect(create_profile, sender=User)

class CusUsers(models.Model):
    Userid = models.CharField(max_length = 12, primary_key = True)
    Username = models.TextField(max_length = 100)
    Useremail = models.EmailField()
    Userphone = models.CharField(max_length = 12)

    def __str__(self):
        return self.Userid

class Item(models.Model):
    Itemid = models.CharField(max_length = 6, primary_key = True)
    Itemname = models.TextField(max_length = 100)
    Itemquantity = models.IntegerField()
    Itemdescription = models.TextField(max_length = 100)

    def __str__(self):
        return self.Itemid

class Employee(models.Model):
    Employeeid = models.CharField(max_length = 8, primary_key = True)
    Employeename = models.TextField(max_length = 100)
    Employeephone = models.CharField(max_length = 12)

    def __str__(self):
        return self.Employeeid

class Booking(models.Model):
    Itemid = models.ForeignKey(Item, on_delete=models.CASCADE)
    Datebooking = models.DateField()
    Datereturn = models.DateField()
    TotalQuantity = models.IntegerField()
    ExpireDate = models.DateField()


models