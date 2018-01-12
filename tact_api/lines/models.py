from django.db import models

from core.models import TimeStampedModel


class Line(TimeStampedModel):
    """
    This class represents a timeline.
    """
    owner = models.ForeignKey('auth.User', related_name='lines', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True, default='')

    class Meta:
        """
        orders created lines in descending order from oldest to newest.
        """
        ordering = ('created',)

    def __str__(self):
        """
        returns the titles of created lines
        """
        return self.title


class Event(TimeStampedModel):
    """
    This class represents an event.
    """
    owner = models.ForeignKey('auth.User', related_name='events', on_delete=models.CASCADE)
    line = models.ForeignKey(Line, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    desc = models.TextField()
    start = models.DateTimeField()
    end = models.DateTimeField()

    class Meta:
        """
        orders created lines in descending order from oldest to newest.
        """
        ordering = ('created',)

    def __str__(self):
        """
        returns the titles of created events
        """
        return self.title
