from django.contrib import admin
from .models import Available_product_table, Sold_product_table

# Register your models here.
admin.site.register(Available_product_table)
admin.site.register(Sold_product_table)