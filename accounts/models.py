from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    address1 = models.CharField(max_length=250,null=True,blank=True)
    address2 = models.CharField(max_length=250,null=True,blank=True)
    pincode = models.CharField(max_length=6,null=True,blank=True)
    landmark = models.CharField(max_length=200,null=True,blank=True)
