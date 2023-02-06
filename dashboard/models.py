from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Available_product_table(models.Model):
    product_name = models.CharField(max_length=50)
    product_price = models.IntegerField()
    product_quantity = models.IntegerField()
    added_by = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)


    def __str__(self):
        return f"{self.id} - {self.product_name} - {self.product_price} - {self.product_quantity} - {self.added_by}"


class Sold_product_table(models.Model):
    date_time = models.DateTimeField(auto_now=True)
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=50)
    product_price = models.IntegerField()
    product_quantity = models.IntegerField()
    sold_by = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return f"{self.id} - {self.date_time} - {self.product_id} - {self.product_name} - {self.product_price} - {self.product_quantity}"


class Store(models.Model):
    name = models.CharField(max_length=250)
    owner = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)

    class Meta:
        unique_together = ["name","owner"]

