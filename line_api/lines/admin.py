from django.contrib import admin

from .models import Announcement, Event, Task

admin.site.register(Announcement)
admin.site.register(Event)
admin.site.register(Task)
