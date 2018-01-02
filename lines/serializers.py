from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Line


class UserSerializer(serializers.HyperlinkedModelSerializer):
    lines = serializers.HyperlinkedRelatedField(many=True, view_name='line-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'lines')


class LineSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Line
        fields = ('url', 'id', 'owner', 'title', 'created')

    def create(self, validated_data):
        """
        Create and return a new 'Line' instance, given the validated data.
        """
        return Line.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing 'Line' instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.save()
        return instance
