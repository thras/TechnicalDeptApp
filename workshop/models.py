from django.conf import settings
from django.db import models

class Vehicle(models.Model):
    '''
    Vehicle model
    
    :model:`Vehicle`.
    '''
    vehicle_id = models.CharField(max_length=30, null=False, unique=True)
    vehicle_sn = models.CharField(max_length=30, unique=True)
    vehicle_type = models.CharField(max_length=30)

    def __str__(self):
        return self.vehicle_id

class Repair(models.Model):
    '''
    Repair model
    
    :model:`Repair`.

    :ForeignKey:`broken_vehicle` from model `Vehicle` - `vehicle_id`.

    :ForeignKey:`author` from model `CustomUser` - `username`.   
    '''
    REPAIR_STATUS = (
        ('Waiting parts', 'Waiting parts'),
        ('Stand by', 'Stand by'),
        ('Incomplete', 'Incomplete'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled')
    )
    repair_title = models.CharField(max_length=50)
    broken_vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    issue = models.TextField(max_length=500)
    repairs_made = models.TextField(null=True,blank=True, max_length=250)
    repair_status = models.CharField(max_length=20, default="Stand by", choices=REPAIR_STATUS, null=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.repair_title} - {self.broken_vehicle}"