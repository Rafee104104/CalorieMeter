from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    User = {
        ('male','Male'),
        ('female','Female')
    }
    user_type = models.CharField(max_length=40,choices=User,null=True)
    
    def __int__(self):
        return self.username
#  Name, Age, Gender, Height, Weight   input daily consumed calories (Item name, Calorie consumed) 
class UserInfo(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.DO_NOTHING, related_name='userinfo')
    Name = models.CharField(max_length=60,blank=True,null=True)
    Age = models.IntegerField(blank=True,null=True)
    Gender = models.CharField(max_length=60,blank=True,null=True)
    Height = models.FloatField(blank=True,null=True)
    Weight = models.FloatField(blank=True,null=True)

    def __str__(self):
        return self.Name

class CalorieInfo(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, related_name='calorieinfo')
    Item_Name = models.CharField(max_length=60,blank=True,null=True)
    Calorie_Consumed = models.FloatField(blank=True,null=True)

    def __str__(self):
        return self.Item_Name