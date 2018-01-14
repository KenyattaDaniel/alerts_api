from django.contrib.auth.models import User

from rest_framework import permissions
from rest_framework import viewsets

from .models import Line, Event
from .serializers import LineSerializer, UserSerializer, EventSerializer
from .permissions import IsOwnerOrReadOnly


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Provides 'list' and 'detail' views of users.

    Authenticated users can see list, details of all active users.
    """
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)
    queryset = User.objects.all()
    serializer_class = UserSerializer

    class Meta:
        ordering = ('id',)


class LineViewSet(viewsets.ModelViewSet):
    """
    Provides 'list', 'create', 'retrieve', 'update' and
    'destroy' actions for lines.

    Authenticated users can see list, details of all created lines.

    Authenticated users can only edit their own lines.
    """
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)
    queryset = Line.objects.all()
    serializer_class = LineSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class EventViewSet(viewsets.ModelViewSet):
    """
    Provides 'list', 'create', 'retrieve', 'update' and
    'destroy' actions for events.

    Authenticated users can see list, details of all created events.

    Authenticated users can create events, add them to
    owned lines and edit them.
    """
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
