from django.db import models

from core.models import TimeStampedModel


class Announcement(TimeStampedModel):
    """
    Class representation of an announcement.
    """
    owner = models.ForeignKey('auth.User', related_name='announcements', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True, default='')
    desc = models.TextField()

    class Meta:
        ordering = ('created',)

    def __str__(self):
        """
        returns string representation of an announcement.
        """
        return self.title


class Event(TimeStampedModel):
    """
    Class representation of an event.
    """
    owner = models.ForeignKey('auth.User', related_name='events', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True, default='')
    desc = models.TextField()
    start = models.DateTimeField()
    end = models.DateTimeField()

    class Meta:
        ordering = ('end',)

    def __str__(self):
        """
        returns string representation of an event.
        """
        return self.title


class Task(TimeStampedModel):
    """
    Class representation of a task.
    """
    owner = models.ForeignKey('auth.User', related_name='tasks', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True, default='')
    desc = models.TextField()
    due = models.DateTimeField()

    class Meta:
        ordering = ('due',)

    def __str__(self):
        """
        returns string representation of a task.
        """
        return self.title
