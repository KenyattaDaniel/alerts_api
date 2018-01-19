from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone

from lines.models import Line, Event


class LineTestCase(TestCase):
    """
    Define the test suite for the Line model.
    """
    def setUp(self):
        """
        Define the line test user and other test variables.
        """
        self.user = User.objects.create(username="tactician")
        self.line_title = "Title goes here"
        self.line = Line(title=self.line_title, owner=self.user)

    def tearDown(self):
        """
        Delete created user after test completion.
        """
        self.user.delete()

    def test_model_can_create_a_line(self):
        """
        Test if the line model can create a line object.
        """
        old_count = Line.objects.count()
        self.line.save()
        new_count = Line.objects.count()
        self.assertNotEqual(old_count, new_count)


class EventTestCase(TestCase):
    """
    Define the test suite for the Event model.
    """
    def setUp(self):
        """
        Define the even test client and other test variables.
        """
        self.user = User.objects.create(username="tactician")

        # create and save a new line
        self.line_title = "Title goes here"
        self.line = Line(title=self.line_title, owner=self.user)
        self.line.save()

        # create a new event linked to the new line
        self.event_title = "Title goes here"
        self.event_desc = "Description goes here."
        self.event_start = timezone.now()
        self.event_end = timezone.now()
        self.event = Event(line=self.line, title=self.event_title, desc=self.event_desc,
                           start=self.event_start, end=self.event_end, owner=self.user)

    def tearDown(self):
        """
        Delete created user after test completion.
        """
        self.user.delete()

    def test_model_can_create_an_event(self):
        """
        Test if event model can create an event object.
        """
        old_count = Event.objects.count()
        self.event.save()
        new_count = Event.objects.count()
        self.assertNotEqual(old_count, new_count)
