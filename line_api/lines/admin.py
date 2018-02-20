from django.contrib import admin

from .models import Line, Announcement, Meeting, Task

admin.site.register(Line)
admin.site.register(Announcement)
admin.site.register(Meeting)
admin.site.register(Task)
