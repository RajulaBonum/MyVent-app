from django.test import TestCase

# Create your tests here.
# events/urls.py

from django.urls import path, include
from . import views
from users import views as user_views 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('event_list', views.event_list, name='event-list'),
    path('event/<int:pk>/', views.event_detail, name='event-detail'),
    path('event/create/', views.create_event, name='create-event'),
    path('event/<int:pk>/edit/', views.update_event, name='update-event'),
    path('event/<int:pk>/delete/', views.delete_event, name='delete-event'),
    path('event/<int:pk>/rsvp/', views.rsvp_event, name='rsvp-event'),
    path('event/<int:pk>/rsvp-list/', views.rsvp_list, name='rsvp-list'),
    path('accounts/profile/', user_views.profile, name='profile'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='users/login.html')),
]

######################
# events/views.py

"""
    views for handling event sessions
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import EventForm, RSVPForm, EventSearchForm
from .utils import send_rsvp_confirmation_email
from .models import Event, RSVP
from django.db.models import Q
from rest_framework import viewsets
from .serializers import EventSerializer



@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = request.user
            event.save()
            messages.success(request, 'Your event has been created!')
            return redirect('event-list')
    else:
        form = EventForm()
    return render(request, 'events/event_form.html', {'form': form})

@login_required
def update_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.user != event.organizer:
        messages.warning(request, 'You are not allowed to edit this event!')
        return redirect('event-list')
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your event has been updated!')
            return redirect('event-list')
    else:
        form = EventForm(instance=event)
    return render(request, 'events/event_form.html', {'form': form})

@login_required
def delete_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.user != event.organizer:
        messages.warning(request, 'You are not allowed to delete this event!')
        return redirect('event-list')
    if request.method == 'POST':
        event.delete()
        messages.success(request, 'Your event has been deleted!')
        return redirect('event-list')
    return render(request, 'events/event_confirm_delete.html', {'event': event})

def event_list(request):
    form = EventSearchForm(request.GET or None)
    events = Event.objects.all()

    if form.is_valid():
        # Filter by title
        if form.cleaned_data.get('title'):
            events = events.filter(title__icontains=form.cleaned_data['title'])

        # Filter by location
        if form.cleaned_data.get('location_name'):
            events = events.filter(location_name__icontains=form.cleaned_data['location_name'])

        # Filter by date range
        if form.cleaned_data.get('date_from'):
            events = events.filter(date__gte=form.cleaned_data['date_from'])
        if form.cleaned_data.get('date_to'):
            events = events.filter(date__lte=form.cleaned_data['date_to'])

        # Filter by category
        if form.cleaned_data.get('category'):
            events = events.filter(category=form.cleaned_data['category'])

    return render(request, 'events/event_list.html', {'events': events, 'form': form})

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'events/event_detail.html', {'event': event})

def home(request):
    return render(request, 'events/home.html')

@login_required
def rsvp_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    rsvp, created = RSVP.objects.get_or_create(user=request.user, event=event)

    if request.method == 'POST':
        form = RSVPForm(request.POST, instance=rsvp)
        if form.is_valid():
            if event.max_attendees and RSVP.objects.filter(event=event, status='attending').count() >= event.max_attendees:
                messages.warning(request, 'The event has reached maximum capacity!')
            else:
                form.save()
                messages.success(request, f'Your RSVP status has been updated to "{rsvp.status}".')
                return redirect('event-detail', pk=event.pk)
    else:
        form = RSVPForm(instance=rsvp)

    return render(request, 'events/rsvp_form.html', {'form': form, 'event': event})

@login_required
def rsvp_list(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.user != event.organizer:
        messages.warning(request, 'Only the event organizer can view RSVP details.')
        return redirect('event-detail', pk=pk)

    rsvps = RSVP.objects.filter(event=event, status='attending')
    return render(request, 'events/rsvp_list.html', {'event': event, 'rsvps': rsvps})

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer