from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from . import views

# Create a router and register viewsets with it.
router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'lines', views.LineViewSet)

# Automatically determine API URLS
urlpatterns = [
    url(r'^', include(router.urls))
]
