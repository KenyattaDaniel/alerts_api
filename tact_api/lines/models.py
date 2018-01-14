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


class Event(TimeStampedModel):
    """
    Class representation of an event.
    """
    owner = models.ForeignKey('auth.User', related_name='events', on_delete=models.CASCADE)
    line = models.ForeignKey(Line, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True, default='')
    desc = models.TextField()
    start = models.DateTimeField()
    end = models.DateTimeField()

    class Meta:
        ordering = ('created',)

    def __str__(self):
        """
        returns string representation of an event.
        """
        return self.title
