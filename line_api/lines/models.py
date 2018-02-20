from django.db import models

from core.models import TimeStampedModel


class Line(TimeStampedModel):
    """
    Class representation of a timeline.
    """
    owner = models.ForeignKey('auth.User', related_name='lines', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True, default='')

    class Meta:
        ordering = ('created',)

    def __str__(self):
        """
        returns string representation of timeline
        """
        return self.title


class Announcement(TimeStampedModel):
    """
    Class representation of an announcement.
    """
    owner = models.ForeignKey('auth.User', related_name='announcements', on_delete=models.CASCADE)
    line = models.ForeignKey(Line, related_name='announcements', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True, default='')
    desc = models.TextField()

    class Meta:
        ordering = ('created',)

    def __str__(self):
        """
        returns string representation of an announcement.
        """
        return self.title


class Meeting(TimeStampedModel):
    """
    Class representation of an meeting.
    """
    owner = models.ForeignKey('auth.User', related_name='meetings', on_delete=models.CASCADE)
    line = models.ForeignKey(Line, related_name='meetings', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True, default='')
    desc = models.TextField()
    start = models.DateTimeField()
    end = models.DateTimeField()

    class Meta:
        ordering = ('end',)

    def __str__(self):
        """
        returns string representation of an meeting.
        """
        return self.title


class Task(TimeStampedModel):
    """
    Class representation of a task.
    """
    owner = models.ForeignKey('auth.User', related_name='tasks', on_delete=models.CASCADE)
    line = models.ForeignKey(Line, related_name='tasks', on_delete=models.CASCADE)
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
