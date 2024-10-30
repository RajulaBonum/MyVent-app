"""
URL configuration for myvent project.
"""

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('events.urls')),
    path('users', include('users.urls')),
]
