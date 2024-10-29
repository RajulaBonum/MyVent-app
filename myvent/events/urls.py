# events/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event-list'),
    path('event/<int:pk>/', views.event_detail, name='event-detail'),
    path('event/create/', views.create_event, name='create-event'),
    path('event/<int:pk>/edit/', views.update_event, name='update-event'),
    path('event/<int:pk>/delete/', views.delete_event, name='delete-event'),
]
