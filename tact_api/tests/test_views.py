from django.contrib.auth.models import User
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.utils import timezone
from rest_framework.test import APIClient
from rest_framework import status

from lines.models import Line, Event


class LineViewTestCase(TestCase):
    """
    Test suite for the Line API views
    """
    def setUp(self):
        """
        Define the line test client and other test variables.
        """
        user = User.objects.create(username="tactician")

        # initialize client and force authentication
        self.client = APIClient()
        self.client.force_authenticate(user=user)

        # create and post a new line using authorized user
        self.line_data = {'title': 'Title goes here'}
        self.response = self.client.post(reverse('line-list'), self.line_data, format='json')

    def test_api_can_create_a_line(self):
        """
        Test the api has line creation capability.
        """
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_authorization_is_enforced(self):
        """
        Test that the api has user authorization.
        """
        line = Line.objects.get()
        new_client = APIClient()
        response = new_client.get('/lines/', kwargs={'pk': line.id}, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_api_can_get_a_line(self):
        """
        Test the api can get a given line.
        """
        line = Line.objects.get()
        response = self.client.get('/lines/', kwargs={'pk': line.id}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, line)

    def test_api_can_update_line(self):
        """
        Test the api can update a given line.
        """
        line = Line.objects.get()
        update_line = {'title': 'New title goes here'}
        response = self.client.put(
            reverse('line-detail', kwargs={'pk': line.id}), update_line, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_delete_line(self):
        """
        Test the api can delete a line.
        """
        line = Line.objects.get()
        response = self.client.delete(reverse('line-detail', kwargs={'pk': line.id}),
                                      format='json', follow=True)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)


class EventViewTestCase(TestCase):
    """
    Test suite for Event API views
    """
    def setUp(self):
        """
        Define the event test client and other test variables.
        """
        user = User.objects.create(username="tactician")

        # initialize client and force authentication
        self.client = APIClient()
        self.client.force_authenticate(user=user)

        # create and post a new line using authorized user
        self.line_data = {'title': 'Title goes here'}
        self.res = self.client.post(reverse('line-list'), self.line_data, format='json')

        # create and post a new event, linked to line created above
        line = Line.objects.get()
        self.event_data = {'line': line.id, 'title': 'Title goes here',
                           'desc': 'Desc. here', 'start': timezone.now(), 'end': timezone.now()}
        self.response = self.client.post(reverse('event-list'), self.event_data, format='json')

    def test_api_can_create_an_event(self):
        """
        Test the api has event creation capability.
        """
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_authorization_is_enforced(self):
        """
        Test that the api has user authorization.
        """
        event = Event.objects.get()
        new_client = APIClient()
        response = new_client.get('/events/', kwargs={'pk': event.id}, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_api_can_get_a_event(self):
        """
        Test the api can get a given event.
        """
        event = Event.objects.get()
        response = self.client.get('/events/', kwargs={'pk': event.id}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, event)

    def test_api_can_update_line(self):
        """
        Test the api can update a given event.
        """
        # get the created line, event
        line = Line.objects.get()
        event = Event.objects.get()

        # perform put request to update event
        update_event = {'line': line.id, 'title': 'Title goes here', 'desc': 'Desc. here',
                        'start': timezone.now(), 'end': timezone.now()}
        response = self.client.put(
            reverse('event-detail', kwargs={'pk': event.id}), update_event, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_delete_event(self):
        """
        Test the api can delete a event.
        """
        event = Event.objects.get()
        response = self.client.delete(reverse('event-detail', kwargs={'pk': event.id}),
                                      format='json', follow=True)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
