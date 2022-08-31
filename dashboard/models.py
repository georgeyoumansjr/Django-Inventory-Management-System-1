from itertools import product
from django.db import models

# Create your models here.

class Available_product_table(models.Model):
    product_name = models.CharField(max_length=50)
    product_price = models.CharField(max_length=50)
    product_quantity = models.IntegerField()