from django.test import TestCase
from .models import Vehicle, Repair
from accounts.models import CustomUser

class VehicleTests(TestCase):
    '''
    Testing Vehicle model

    :model:`Vehicle`.
    '''
    @classmethod
    def setUpTestData(cls):
        
        cls.vehicle = Vehicle.objects.create(
                vehicle_id = "Lift No1",
                vehicle_sn = "AB-123",
                vehicle_type = "Lift",
         )
        
    def test_vehicle_content(self):
        self.assertEqual(self.vehicle.vehicle_id, "Lift No1")
        self.assertEqual(self.vehicle.vehicle_sn, "AB-123")
        self.assertEqual(self.vehicle.vehicle_type, "Lift")

class RepairTests(TestCase):
    '''
    Testing Repair model

    :model:`Repair`.
    '''
    @classmethod
    def setUpTestData(cls):
        '''
        The Repair model have ForeignKeys at broken_vehicle and author fields,

        so we need to create a user and a vehicle instance to test it.
        '''
        user = CustomUser.objects.create(
            username = "User1",
        )

        vehicle = Vehicle.objects.create(
                vehicle_id = "Lift No1"
         )
        
        cls.repair = Repair.objects.create(
            repair_title = "Broken axle",
            broken_vehicle = vehicle,
            issue = "rear axle is broken",
            repair_status = 'Cancelled',
            repairs_made = "new axle",
            author = user,
            )
        
    def test_order_content(self):
        self.assertEqual(self.repair.repair_title, "Broken axle")
        self.assertEqual(self.repair.broken_vehicle.vehicle_id, "Lift No1")
        self.assertEqual(self.repair.issue, "rear axle is broken")
        self.assertEqual(self.repair.repair_status, "Cancelled")
        self.assertEqual(self.repair.repairs_made, "new axle")
        self.assertEqual(self.repair.author.username, "User1")