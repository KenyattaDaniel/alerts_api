from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Line, Event


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    Convert User model instances into native Python datatypes to be rendered as JSON.
    """
    lines = serializers.HyperlinkedRelatedField(many=True, view_name='line-detail', read_only=True)

    class Meta:
        """
        list configuration attributes for UserSerializer class
        """
        model = User
        fields = ('url', 'id', 'username', 'lines')


class LineSerializer(serializers.HyperlinkedModelSerializer):
    """
    Convert Line model instances into native Python datatypes to be rendered as JSON.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        """
        list configuration attributes for LineSerializer class
        """
        model = Line
        fields = ('url', 'id', 'owner', 'created', 'title')

    def create(self, validated_data):
        """
        create and return a new 'Line' instance, given the validated data.
        """
        return Line.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        update and return an existing 'Line' instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.save()
        return instance


class EventSerializer(serializers.HyperlinkedModelSerializer):
    """
    Convert Event model instances into native Python datatypes to be rendered as JSON.
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """
        list configuration attributes for EventSerializer class
        """
        model = Event
        fields = ('url', 'id', 'created', 'owner', 'title', 'desc', 'start', 'end', 'line')

    def create(self, validated_data):
        """
        create and return a new 'Event' instance, given the validated data.
        """
        return Event.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        update and return an existing 'Event' instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.desc = validated_data.get('desc', instance.desc)
        instance.start = validated_data.get('start', instance.start)
        instance.end = validated_data.get('end', instance.end)
        instance.line = validated_data.get('line', instance.line)
        instance.save()
        return instance
