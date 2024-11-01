"""
events/forms.py
    To handle creating and editing events
"""

from django import forms
from .models import RSVP
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'location_name', 'date', 'max_attendees']
        widgets = {
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
        }

class RSVPForm(forms.ModelForm):
    class Meta:
        model = RSVP
        fields = ['status']  # Users can choose 'attending' or 'not attending'


class EventSearchForm(forms.Form):
    title = forms.CharField(required=False, label='Search by Title')
    location_name = forms.CharField(required=False, label='Search by Location')
    date_from = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label='Date From')
    date_to = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label='Date To')
    
    category = forms.ChoiceField(
        required=False,
        choices=[('', 'All Categories')] + list(Event.CATEGORY_CHOICES),
        label='Filter by Category'
    )

