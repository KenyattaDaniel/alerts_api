from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Line, Event


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    Convert User model instance into native Python datatypes to be rendered as JSON.
    """
    lines = serializers.HyperlinkedRelatedField(many=True, view_name='line-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'lines')


class LineSerializer(serializers.HyperlinkedModelSerializer):
    """
    Convert Line model instance into native Python datatypes to be rendered as JSON.
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Line
        fields = ('url', 'id', 'owner', 'created', 'modified', 'title')

    def create_line(self, validated_data):
        """
        create and return a new Line object with validated data.
        """
        return Line.objects.create(**validated_data)

    def update_line(self, instance, validated_data):
        """
        update and return an existing line object with validated.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.save()
        return instance


class EventSerializer(serializers.HyperlinkedModelSerializer):
    """
    Convert Event model instance into native Python datatypes to be rendered as JSON.
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Event
        fields = ('url', 'id', 'owner', 'line', 'created', 'modified', 'title', 'desc', 'start',
                  'end')

    def get_fields(self, *args, **kwargs):
        """
        create and return a new Event object (linked to a user owned Line) with validated data.

        update and return an existing Event object with validated data.
        """
        fields = super(EventSerializer, self).get_fields(*args, **kwargs)
        view = self.context['view']
        owner = view.request.user
        fields['line'].queryset = fields['line'].queryset.filter(owner=owner)
        return fields
