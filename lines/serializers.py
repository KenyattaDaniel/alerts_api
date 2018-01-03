from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Line


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    Converts User model instances into native Python datatypes to be rendered as JSON. 
    """
    lines = serializers.HyperlinkedRelatedField(many=True, view_name='line-detail', read_only=True)

    class Meta:
        """
        lists the url, id, username and created lines of a user.
        """
        model = User
        fields = ('url', 'id', 'username', 'lines')


class LineSerializer(serializers.HyperlinkedModelSerializer):
    """
    Converts Line model instances into native Python datatypes to be rendered as JSON. 
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """
        lists the url, id, owner, title and created date of a line.
        """
        model = Line
        fields = ('url', 'id', 'owner', 'title', 'created')

    def create(self, validated_data):
        """
        creates and returns a new 'Line' instance, given the validated data.
        """
        return Line.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        updates and returns an existing 'Line' instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.save()
        return instance
