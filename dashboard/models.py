from datetime import datetime
from django.db import models

# Create your models here.

class Available_product_table(models.Model):
    product_name = models.CharField(max_length=50)
    product_price = models.IntegerField()
    product_quantity = models.IntegerField()

    def __str__(self):
        return f"{self.id} - {self.product_name} - {self.product_price} - {self.product_quantity}"


class Sold_product_table(models.Model):
    date_time = models.DateTimeField(auto_now=True)
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=50)
    product_price = models.IntegerField()
    product_quantity = models.IntegerField()

    def __str__(self):
        return f"{self.id} - {self.date_time} - {self.product_id} - {self.product_name} - {self.product_price} - {self.product_quantity}"
