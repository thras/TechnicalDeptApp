from django.test import TestCase
from django.urls import reverse
from .models import CustomUser

class UserTests(TestCase):
    '''
    Testing user model

    :model:`CustomUser`.
    '''
    @classmethod
    def setUpTestData(cls):
        
        cls.user = CustomUser.objects.create(
                username = 'dummyUser',
                is_superuser = False,
                is_staff = True,
                is_technician = True,
                is_orderer = False,
                is_observer = False,
         )
        
    def test_user_content(self):
        self.assertEqual(self.user.username, "dummyUser")
        self.assertEqual(self.user.is_superuser, False)
        self.assertEqual(self.user.is_staff, True)
        self.assertEqual(self.user.is_technician, True)
        self.assertEqual(self.user.is_orderer, False)
        self.assertEqual(self.user.is_observer, False)





