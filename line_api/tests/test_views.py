from django.contrib.auth.models import User
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.utils import timezone
from rest_framework.test import APIClient
from rest_framework import status

from lines.models import Announcement, Event, Task


class AnnouncementViewTestCase(TestCase):
    """
    Test suite for Announcement API views
    """
    def setUp(self):
        """
        Define the announcement test client and other test variables.
        """
        user = User.objects.create(username="tactician")

        # initialize client and force authentication
        self.client = APIClient()
        self.client.force_authenticate(user=user)

        # create and post a new announcement, linked to line created above
        self.announ_data = {'title': 'Title goes here', 'desc': 'Desc. here'}
        self.response = self.client.post(reverse('announcement-list'),
                                         self.announ_data, format='json')

    def test_api_can_create_a_announcement(self):
        """
        Test the api has event creation capability.
        """
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_authorization_is_enforced(self):
        """
        Test that the api has unauthroized user access.
        """
        announ = Announcement.objects.get()
        new_client = APIClient()
        response = new_client.get('/announcements/', kwargs={'pk': announ.id}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_get_a_announcement(self):
        """
        Test the api can get a given announcement.
        """
        announ = Announcement.objects.get()
        response = self.client.get('/announcements/', kwargs={'pk': announ.id}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, announ)

    def test_api_can_update_announcement(self):
        """
        Test the api can update a given announcement.
        """
        # get the created announcement
        announ = Announcement.objects.get()

        # perform put request to update event
        update_announ = {'title': 'Title goes here', 'desc': 'Desc. here'}
        response = self.client.put(
            reverse('announcement-detail', kwargs={'pk': announ.id}), update_announ, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_delete_announcement(self):
        """
        Test the api can delete an announcement.
        """
        announ = Announcement.objects.get()
        response = self.client.delete(reverse('announcement-detail', kwargs={'pk': announ.id}),
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

        # create and post a new event, linked to line created above
        self.event_data = {'title': 'Title goes here',
                           'desc': 'Desc. here', 'start': timezone.now(), 'end': timezone.now()}
        self.response = self.client.post(reverse('event-list'), self.event_data, format='json')

    def test_api_can_create_a_event(self):
        """
        Test the api has event creation capability.
        """
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_authorization_is_enforced(self):
        """
        Test that the api has unauthorized user access.
        """
        event = Event.objects.get()
        new_client = APIClient()
        response = new_client.get('/events/', kwargs={'pk': event.id}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_get_a_event(self):
        """
        Test the api can get a given event.
        """
        event = Event.objects.get()
        response = self.client.get('/events/', kwargs={'pk': event.id}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, event)

    def test_api_can_update_event(self):
        """
        Test the api can update a given event.
        """
        # get the created event
        event = Event.objects.get()

        # perform put request to update event
        update_event = {'title': 'Title goes here', 'desc': 'Desc. here',
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


class TaskViewTestCase(TestCase):
    """
    Test suite for Task API views
    """
    def setUp(self):
        """
        Define the task test client and other test variables.
        """
        user = User.objects.create(username="tactician")

        # initialize client and force authentication
        self.client = APIClient()
        self.client.force_authenticate(user=user)

        # create and post a new event, linked to line created above
        self.task_data = {'title': 'Title goes here', 'desc': 'Desc. here',
                          'due': timezone.now()}
        self.response = self.client.post(reverse('task-list'), self.task_data, format='json')

    def test_api_can_create_a_task(self):
        """
        Test the api has task creation capability.
        """
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_authorization_is_enforced(self):
        """
        Test that the api has unauthorized user access.
        """
        task = Task.objects.get()
        new_client = APIClient()
        response = new_client.get('/tasks/', kwargs={'pk': task.id}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_get_a_task(self):
        """
        Test the api can get a given task.
        """
        task = Task.objects.get()
        response = self.client.get('/tasks/', kwargs={'pk': task.id}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, task)

    def test_api_can_update_task(self):
        """
        Test the api can update a given task.
        """
        # get the created task
        task = Task.objects.get()

        # perform put request to update event
        update_task = {'title': 'Title goes here', 'desc': 'Desc. here',
                       'due': timezone.now()}
        response = self.client.put(
            reverse('task-detail', kwargs={'pk': task.id}), update_task, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_delete_task(self):
        """
        Test the api can delete a task.
        """
        task = Task.objects.get()
        response = self.client.delete(reverse('task-detail', kwargs={'pk': task.id}),
                                      format='json', follow=True)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
