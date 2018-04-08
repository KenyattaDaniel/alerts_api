from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from . import views

# Create a router and register viewsets with it.
router = DefaultRouter()
router.register(r'users', views.UserViewSet, base_name='user')
router.register(r'announcements', views.AnnouncementViewSet, base_name='announcement')
router.register(r'events', views.EventViewSet, base_name='event')
router.register(r'tasks', views.TaskViewSet, base_name='task')

# Automatically determine API URLS
urlpatterns = [
    url(r'^', include(router.urls))
]
