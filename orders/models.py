from django.conf import settings
from django.db import models

class Supplier(models.Model):
    '''
    Supplier model
    
    :model:`Supplier`.
    '''
    supplier_name = models.CharField(max_length=50, null=False, unique=True)
    address = models.CharField(max_length=75)
    vat = models.CharField(max_length=20, unique=True)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.supplier_name

class Order(models.Model):
    '''
    Order model
    
    :model:`Order`.
    
    :ForeignKey:`order_supplier` from model `Supplier` - `supplier_name`.

    :ForeignKey:`author` from model `CustomUser` - `username`.
    '''
    ORDER_STATUS = (
        ('Waiting Offer', 'Waiting Offer'),
        ('Awaiting Delivery', 'Awaiting Delivery'),
        ('Incomplete', 'Incomplete'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled')
    )

    order = models.CharField(max_length=50, verbose_name="Order title")
    order_supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    body = models.TextField(max_length=500, verbose_name="Ordered goods")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    order_status = models.CharField(max_length=20, default="Waiting Offer", choices=ORDER_STATUS, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.order
