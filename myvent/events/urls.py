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
