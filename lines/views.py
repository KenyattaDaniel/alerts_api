from django.contrib.auth.models import User

from rest_framework import permissions
from rest_framework import viewsets

from .models import Line
from .serializers import LineSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Provides 'list' and 'detail' information of users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LineViewSet(viewsets.ModelViewSet):
    """
    Provides 'list', 'create', 'retrieve', 'update' and
    'destroy' actions for lines.
    """
    queryset = Line.objects.all()
    serializer_class = LineSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
