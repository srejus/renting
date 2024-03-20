from django.db import models
from renting.models import RentedItem
from accounts.models import Account

# Create your models here.
class Earning(models.Model):
    user = models.ForeignKey(Account,on_delete=models.CASCADE,related_name='delivery_earning')
    item = models.ForeignKey(RentedItem,on_delete=models.CASCADE,related_name='delivery_item')
    earning = models.FloatField(default=50.0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)+" > "+str(self.earning)
