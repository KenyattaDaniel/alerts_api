from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone

from lines.models import Announcement, Event, Task


class AnnouncementTestCase(TestCase):
    """
    Define the test suite for the Announcement model.
    """
    def setUp(self):
        """
        Define the announcement test client and other test variables.
        """
        self.user = User.objects.create(username="tactician")

        # create an announcement
        self.announ_title = "Title goes here"
        self.announ_desc = "Description goes here."
        self.announ = Announcement(title=self.announ_title, desc=self.announ_desc,
                                   owner=self.user)

    def tearDown(self):
        """
        Delete created user after test completion.
        """
        self.user.delete()

    def test_model_can_create_a_announcement(self):
        """
        Test if Announcement model can create an announcement object.
        """
        old_count = Announcement.objects.count()
        self.announ.save()
        new_count = Announcement.objects.count()
        self.assertNotEqual(old_count, new_count)


class EventTestCase(TestCase):
    """
    Define the test suite for the Event model.
    """
    def setUp(self):
        """
        Define the event test client and other test variables.
        """
        self.user = User.objects.create(username="tactician")

        # create an event linked to the new line
        self.event_title = "Title goes here"
        self.event_desc = "Description goes here."
        self.event_start = timezone.now()
        self.event_end = timezone.now()
        self.event = Event(title=self.event_title, desc=self.event_desc,
                           start=self.event_start, end=self.event_end, owner=self.user)

    def tearDown(self):
        """
        Delete created user after test completion.
        """
        self.user.delete()

    def test_model_can_create_a_event(self):
        """
        Test if Event model can create an event object.
        """
        old_count = Event.objects.count()
        self.event.save()
        new_count = Event.objects.count()
        self.assertNotEqual(old_count, new_count)


class TaskTestCase(TestCase):
    """
    Define the test suite for the Task model.
    """
    def setUp(self):
        """
        Define the task test client and other test variables.
        """
        self.user = User.objects.create(username="tactician")

        # create a task linked to the new line
        self.task_title = "Title goes here"
        self.task_desc = "Description goes here."
        self.task_due = timezone.now()
        self.task = Task(title=self.task_title, desc=self.task_desc,
                         due=self.task_due, owner=self.user)

    def tearDown(self):
        """
        Delete created user after test completion.
        """
        self.user.delete()

    def test_model_can_create_a_task(self):
        """
        Test if Task model can create a task object.
        """
        old_count = Task.objects.count()
        self.task.save()
        new_count = Task.objects.count()
        self.assertNotEqual(old_count, new_count)
