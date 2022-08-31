from django.db import models

# Create your models here.

class Available_product_table(models.Model):
    product_name = models.CharField(max_length=50)
    product_price = models.CharField(max_length=50)
    product_quantity = models.IntegerField()

    def __str__(self):
        return f"{self.id} - {self.product_name} - {self.product_price} - {self.product_quantity}"
