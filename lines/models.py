from django.db import models


class Line(models.Model):
    """
    A digital line that transmits information about key announcements, events and tasks.    
    """
    owner = models.ForeignKey('auth.User', related_name='lines', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.title


class Event(models.Model):
    line = models.ForeignKey(Line, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    desc = models.TextField()
    start = models.DateTimeField()
    end = models.DateTimeField()

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.title
