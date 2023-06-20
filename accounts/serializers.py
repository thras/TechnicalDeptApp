from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    '''
    Abstracted user model.

    Password field removed for security issues.

    :model:`CustomUser`.
    '''
    class Meta:
        fields = (    
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "is_staff",
            "is_active",
            "is_technician",
            "is_orderer",
            "is_observer",)
        model = CustomUser