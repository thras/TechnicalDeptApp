from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    '''
    Abstract the user model of Django adding new custom fields.
     
    First because we can't do it later (after the first migration).

    Second at this project is for permissions and for future updates.
    '''
    is_technician = models.BooleanField(default=False, null=True)
    is_orderer = models.BooleanField(default=False, null=True)
    is_observer = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.username