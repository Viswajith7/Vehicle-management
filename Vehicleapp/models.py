from django.db import models

# Create your models here.
class VehicleDB(models.Model):
    Vehicle_Number = models.CharField(max_length=50,null=True,blank=True)
    Vehicle_Type = models.CharField(max_length=50, null=True, blank=True)
    Vehicle_Model  = models.CharField(max_length=50, null=True, blank=True)
    Vehicle_Description  = models.CharField(max_length=100, null=True, blank=True)




class AdminDB(models.Model):
    Username = models.CharField(max_length=40,null=True,blank=True)
    Email = models.EmailField(max_length=200,null=True,blank=True)
    Password = models.CharField(max_length=40,null=True,blank=True)
    C_Password = models.CharField(max_length=40,null=True,blank=True)





class UserDB(models.Model):
    Username = models.CharField(max_length=40,null=True,blank=True)
    Email = models.EmailField(max_length=200,null=True,blank=True)
    Password = models.CharField(max_length=40,null=True,blank=True)
    C_Password = models.CharField(max_length=40,null=True,blank=True)



