from django.contrib.auth.models import User
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.utils import timezone
from rest_framework.test import APIClient
from rest_framework import status

from .models import Line, Event


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
        self.response = self.client.post(reverse('line-list'), self.line_data, format='json')

    def test_api_can_create_a_line(self):
        """
        Test the api has line creation capability.
        """
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_line(self):
        """
        Test the api can get a given line.
        """
        line = Line.objects.get()
        response = self.client.get(
            reverse('line-detail', kwargs={'pk': line.id}), format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, line)

    def test_api_can_update_line(self):
        """
        Test the api can update a given line.
        """
        line = Line.objects.get()
        update_title = {'title': 'New title goes here'}
        response = self.client.put(
            reverse('line-detail', kwargs={'pk': line.id}), update_title, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_delete_line(self):
        """
        Test the api can delete a line.
        """
        line = Line.objects.get()
        response = self.client.delete(reverse('line-detail', kwargs={'pk': line.id}),
            format='json', follow=True)


class EventLineTestCase(TestCase):
    """
    Test suite for Event API views
    """

    def setUp(self):
        """
        Define the event test client and other test variables.
        """
        # create and authenticate new user, create a new line
        self.client = APIClient()
        self.owner = User.objects.create(username="user1")
        self.client.force_authenticate(user=self.owner)
        self.line_data = {'title': 'Title goes here'}
        self.response = self.client.post(reverse('line-list'), self.line_data, format='json')
        line = Line.objects.get()
        # CONTINUE FROM HERE 
        # specify variables req. for creating a new event
        # event_data = {'title': 'Title goes here', 'desc': 'Description goes here.',
        #                    'start': timezone.now(), 'end': timezone.now()}          
        # self.response = self.client.post(reverse('event-list'), event_data, format='json')

    def test_api_can_create_an_event(self):
        """
        Test the api has event creation capability.
        """
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
