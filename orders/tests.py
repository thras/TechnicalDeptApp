from django.test import TestCase
from django.urls import reverse
from .models import Order, Supplier
from accounts.models import CustomUser


class OrderTests(TestCase):
    '''
    Testing Order model

    :model:`Order`.
    '''
    @classmethod
    def setUpTestData(cls):
        '''
        The Order model have ForeignKeys at order_supplier and author fields,

        so we need to create a user and a supplier instance to test it.
        '''
        user = CustomUser.objects.create(
            username = "dummyUser",
        )

        supplier = Supplier.objects.create(
                supplier_name = 'dummySupplier',
        )
        
        cls.order = Order.objects.create(
            order = "PVC parts",
            author = user,
            order_status = "Completed",
            order_supplier = supplier,
            body = "5*D25 pipes",
            )
        
    def test_order_content(self):
        self.assertEqual(self.order.order, "PVC parts")
        self.assertEqual(self.order.order_supplier.supplier_name, 'dummySupplier')
        self.assertEqual(self.order.body, "5*D25 pipes")
        self.assertEqual(self.order.order_status, "Completed")
        self.assertEqual(self.order.author.username, "dummyUser")

class SupplierTests(TestCase):
    '''
    Testing Supplier model

    :model:`Supplier`.
    '''
    @classmethod
    def setUpTestData(cls):
        
        cls.supplier = Supplier.objects.create(
                supplier_name = 'Supplier1',
                address = "Drama",
                vat = "0123456789",
                phone = "01234567890",
         )
        
    def test_supplier_content(self):
        self.assertEqual(self.supplier.supplier_name, "Supplier1")
        self.assertEqual(self.supplier.address, 'Drama')
        self.assertEqual(self.supplier.vat, "0123456789")
        self.assertEqual(self.supplier.phone, "01234567890")



