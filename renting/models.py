from django.db import models
from accounts.models import Account

# Create your models here.
class Listing(models.Model):
    CATEGORY_CHOICES = (
        ('BOOKS','BOOKS'),
        ('FURNITURE','FURNITURE'),
        ('AUTOMOBILE','AUTOMOBILE'),
        ('GADGETS','GADGETS'),
        ('OTHERS','OTHERS'),
    )
    listed_by = models.ForeignKey(Account,on_delete=models.CASCADE,related_name='item_listed_by')
    item_name = models.CharField(max_length=100)
    rent_price_per_day = models.FloatField(default=0.0)
    item_image = models.ImageField(upload_to='listing_images',null=True)
    location = models.CharField(max_length=100,null=True,blank=True)
    avg_rating = models.DecimalField(default=0.0,max_digits=2,decimal_places=1)
    category = models.CharField(max_length=15,default='OTHERS')
    description = models.CharField(max_length=200,null=True,blank=True)
    is_available = models.BooleanField(default=True)