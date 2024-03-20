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


class RentedItem(models.Model):
    REQUEST_PLACED = 'REQUEST_PLACED'
    ACCEPTED = 'ACCEPTED'
    REJECTED = 'REJECTED'
    STATUS_CHOCIES = (
        (REQUEST_PLACED,REQUEST_PLACED),
        (ACCEPTED,ACCEPTED),
        (REJECTED,REJECTED),
    )
    user = models.ForeignKey(Account,on_delete=models.CASCADE,related_name='rented_by')
    item = models.ForeignKey(Listing,on_delete=models.CASCADE)
    no_of_days = models.IntegerField(default=1)
    qnty = models.IntegerField(default=1)
    full_name = models.CharField(max_length=50,null=True,blank=True)
    phone = models.CharField(max_length=15,null=True,blank=True)
    address = models.CharField(max_length=50,null=True,blank=True)
    pincode = models.CharField(max_length=6,null=True,blank=True)
    landmark = models.CharField(max_length=50,null=True,blank=True)
    status = models.CharField(max_length=50,default='REQUEST_PLACED',choices=STATUS_CHOCIES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.full_name)+">"+str(self.item.item_name)