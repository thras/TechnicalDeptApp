from rest_framework import serializers
from .models import Order, Supplier
from accounts.models import CustomUser
 
class OrderSerializer(serializers.ModelSerializer):
    '''
    Order model serializer.

    :model:`Order`.

    :ForeignKey:`order_supplier` from model `Supplier` - `supplier_name`.

    :ForeignKey:`author` from model `CustomUser` - `username`.
    '''
    # To show the supplier name and not the ID the same for author
    # SlugRelatedField to prevent issues with unique fields (can't edit username and supplier_name)
    order_supplier = serializers.SlugRelatedField(read_only=False, slug_field="supplier_name", queryset=Supplier.objects.all())
    author = serializers.SlugRelatedField(read_only=False, slug_field="username", queryset=CustomUser.objects.all())
    
    class Meta:
        fields = '__all__'
        model = Order

class SupplierSerializer(serializers.ModelSerializer):
    '''
    Supplier model serializer.

    :model:`Supplier`.
    '''
    class Meta:
        fields = '__all__'
        model = Supplier
