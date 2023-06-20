from rest_framework import serializers
from accounts.models import CustomUser
from .models import Vehicle, Repair

class VehicleSerializer(serializers.ModelSerializer):
    '''
    Vehicle model serializer.

    :model:`Vehicle`.
    '''
    class Meta:
        fields = '__all__'
        model = Vehicle

class RepairSerializer(serializers.ModelSerializer):
    '''
    Repair model serializer.
    
    :model:`Repair`.

    :ForeignKey:`broken_vehicle` from model `Vehicle` - `vehicle_id`.

    :ForeignKey:`author` from model `CustomUser` - `username`.   
    '''
    # To show the vehicle name and not the ID the same for author
    # SlugRelatedField to prevent issues with unique fields (can't edit username and vehicle_id)
    broken_vehicle = serializers.SlugRelatedField(read_only=False, slug_field="vehicle_id", queryset=Vehicle.objects.all())
    author = serializers.SlugRelatedField(read_only=False, slug_field="username", queryset=CustomUser.objects.all())
    class Meta:
        fields = '__all__'
        model = Repair