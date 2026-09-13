from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    Gender = {
        ('male','Male'),
        ('female','Female')
    }
    user_type = models.CharField(max_length=40,choices=Gender,null=True)
    display_name = models.CharField(max_length=40,null=True)
    
    def __str__(self):
        return self.username
class UserInfo(models.Model):
    users = models.OneToOneField(CustomUser, on_delete=models.DO_NOTHING, related_name='userinfo',null=True,blank=True)
    Name = models.CharField(max_length=60,blank=True,null=True)
    Age = models.FloatField(blank=True,null=True)
    Gender = models.CharField(max_length=60,blank=True,null=True)
    Height = models.FloatField(blank=True,null=True)
    Weight = models.FloatField(blank=True,null=True)
    bmr = models.FloatField(blank=True,null=True)
    
    
    def __str__(self):
        return self.users.username

class CalorieInfo(models.Model):
    users = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, related_name='calorieinfo',null=True,blank=True)
    Item_Name = models.CharField(max_length=60,blank=True,null=True)
    date = models.DateField(auto_now_add=True)
    Calorie_Consumed = models.FloatField(blank=True,null=True)

    def __str__(self):
        return self.users.username