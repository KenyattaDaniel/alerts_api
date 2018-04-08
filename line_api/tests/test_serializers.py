from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory

from lines.models import Announcement, Event, Task
from lines.serializers import AnnouncementSerializer, EventSerializer, TaskSerializer


# class LineSerializerTestCase(TestCase):
#     """
#     Define the test suite for the Line serializer.
#     """
#     def setUp(self):
#         """
#         Define the line serializer test variables.
#         """
#         # create User object instance
#         self.name = 'tactician'
#         self.user = User.objects.create(username=self.name)

#         # create Request object to pass to LineSerializer 'context' argument
#         factory = APIRequestFactory()
#         self.request = factory.get('/')

#         # specify 
#         self.line_attributes = {
#             'owner': self.user,
#             'title': 'Title goes here'
#         }

#         self.serializer_data = {
#             'owner': self.user,
#             'title': 'This is the title'
#         }

#         self.serializer_context = {
#             'request': self.request
#         }

#         self.line = Line.objects.create(**self.line_attributes)
#         self.serializer = LineSerializer(instance=self.line, context=self.serializer_context)

#     def test_serializer_contains_fields(self):
#         """
#         Test if the serializer has the attributes expected.
#         """
#         data = self.serializer.data
#         self.assertCountEqual(data.keys(), ('url', 'id', 'owner', 'created', 'modified', 'title',
#                                             'announcements', 'events', 'tasks'))

#     def test_owner_field_content(self):
#         """
#         Test if serializer produces the expected data type for owner field.
#         """
#         data = self.serializer.data
#         self.assertEqual(data['owner'], self.name)

#     def test_created_field_content(self):
#         """
#         Test if serializer produces the expected data type for created field.
#         """
#         data = self.serializer.data
#         self.assertEqual(data['created'], timezone.now()) # CONTINUE FROM HERE
