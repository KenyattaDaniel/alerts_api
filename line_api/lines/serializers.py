from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Announcement, Event, Task


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    Convert User model instances' native Python datatypes into and from JSON.
    """
    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'announcements', 'events', 'tasks')


class AnnouncementSerializer(serializers.ModelSerializer):
    """
    Convert Announcement model instances' native Python datatypes into and from JSON.
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Announcement
        fields = ('url', 'id', 'owner', 'created', 'modified', 'title', 'desc')

    def create_announcement(self, validated_data):
        """
        create and return a new announcement object with validated data.
        """
        return Announcement.objects.create(**validated_data)

    def update_announcement(self, instance, validated_data):
        """
        update and return an existing announcement object with validated.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.desc = validated_data.get('desc', instance.desc)
        instance.save()
        return instance


class EventSerializer(serializers.ModelSerializer):
    """
    Convert Event model instances' native Python datatypes into and from JSON.
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Event
        fields = ('url', 'id', 'owner', 'created', 'modified', 'title', 'desc', 'start',
                  'end')

    def create_event(self, validated_data):
        """
        create and return a new event object with validated data.
        """
        return Event.objects.create(**validated_data)

    def update_event(self, instance, validated_data):
        """
        update and return an existing event object with validated.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.desc = validated_data.get('desc', instance.desc)
        instance.start = validated_data.get('start', instance.start)
        instance.end = validated_data.get('end', instance.end)
        instance.save()
        return instance


class TaskSerializer(serializers.ModelSerializer):
    """
    Convert Task model instances' native Python datatypes into and from JSON.
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Task
        fields = ('url', 'id', 'owner', 'created', 'modified', 'title', 'desc', 'due')

    def create_task(self, validated_data):
        """
        create and return a new task object with validated data.
        """
        return Task.objects.create(**validated_data)

    def update_task(self, instance, validated_data):
        """
        update and return an existing task object with validated.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.desc = validated_data.get('desc', instance.desc)
        instance.due = validated_data.get('due', instance.due)
        instance.save()
        return instance


