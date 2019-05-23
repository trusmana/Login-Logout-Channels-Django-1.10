from __future__ import unicode_literals
from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_details = models.TextField()
    harga = models.IntegerField()
    active = models.IntegerField(default='1')

    def __str__(self):
        return '%s (%s tk)' % (self.product_name, self.harga)

class Order(models.Model):
    name = models.CharField(max_length=200)
    telepon = models.CharField(max_length=20)
    Alamat = models.TextField()
    delivery_date = models.DateField(blank=True)
    product_id = models.ForeignKey(Product)
    payment_option = models.CharField(max_length=50)
    order_status = models.CharField(max_length=50)
    qt = models.IntegerField()

