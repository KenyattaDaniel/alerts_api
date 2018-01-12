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
        configuration attributes for UserSerializer class
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
        configuration attributes for LineSerializer class
        """
        model = Line
        fields = ('url', 'id', 'owner', 'created', 'modified', 'title')

    def create_line(self, validated_data):
        """
        create and return a new 'Line' instance, given validated data.
        """
        return Line.objects.create(**validated_data)

    def update_line(self, instance, validated_data):
        """
        update and return an existing 'Line' instance, given validated data.
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
        configuration attributes for EventSerializer class
        """
        model = Event
        fields = ('url', 'id', 'owner', 'line', 'created', 'modified', 'title', 'desc', 'start',
                  'end')

    def get_fields(self, *args, **kwargs):
        """
        create and return a new 'Event' instance linked to a owned 'Line', given validated data.

        update and return an existing 'Event' instance, given the validated data.
        """
        fields = super(EventSerializer, self).get_fields(*args, **kwargs)
        view = self.context['view']
        owner = view.request.user
        fields['line'].queryset = fields['line'].queryset.filter(owner=owner)
        return fields
