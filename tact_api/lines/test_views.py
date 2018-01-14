from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status


class LineViewTestCase(TestCase):
    """
    Test suite for the Line API views
    """

    def setUp(self):
        """
        Define the line test client and other test variables.
        """
        self.client = APIClient()
        self.line_owner = User.objects.create(username="user")
        self.client.force_authenticate(user=self.line_owner)
        self.line_data = {'title': 'Title goes here'}
        self.response = self.client.post(
            '/lines/',
            self.line_data,
            format='json')

    def test_api_can_create_a_line(self):
        """
        Test the api has line creation capability.
        """
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_line(self):
        """
        Test the api can get a given line.
        """
