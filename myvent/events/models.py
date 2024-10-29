# events/models.py

"""
we'll define the event model to capture details like title, description, date, time, location, and max attendees.
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now)
    max_attendees = models.PositiveIntegerField()
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
