from django.test import SimpleTestCase
from django.urls import reverse

'''
Testing home page and the API and front-end login/logout pages.

The other pages have login decorator and I can't test them.
'''

class HomepageTests(SimpleTestCase):
    '''Testing the homepage.'''
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self): 
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)


class AuthAPILoginTests(SimpleTestCase):
    '''Testing API login view.'''
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/api-auth/login/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self): 
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)


class AuthAPILogoutTests(SimpleTestCase):
    '''Testing API logout view.'''
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/api-auth/logout/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self): 
        response = self.client.get(reverse("logout"))
        self.assertEqual(response.status_code, 200)


class AccountsLoginTests(SimpleTestCase):
    '''Testing front-end login view.'''
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/accounts/login/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self): 
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)


class AccountsLogoutTests(SimpleTestCase):
    '''Testing front-end logout view.'''
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/accounts/logout/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self): 
        response = self.client.get(reverse("logout"))
        self.assertEqual(response.status_code, 200)


