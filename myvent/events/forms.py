"""
events/forms.py
    To handle creating and editing events
"""

from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'location', 'date', 'max_attendees']
