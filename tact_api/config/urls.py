"""Tact URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.schemas import get_schema_view
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

# Autogenerate schema view
schema_view = get_schema_view(title='Pastebin API')

# Specify URLS for apps (e.g. lines), Django Admin, Schema
urlpatterns = [
    url(r'^', include('lines.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^schema/$', schema_view),
]

# Specify URLS for JSON Web Token authorization views
urlpatterns += [
    url(r'^api/', include('rest_framework.urls')),
    url(r'^jwt-auth/', obtain_jwt_token),
    url(r'^jwt-auth-refresh/', refresh_jwt_token),
    url(r'^jwt-auth-verify/', verify_jwt_token),
]
