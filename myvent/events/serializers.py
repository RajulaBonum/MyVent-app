# events/serializers.py
from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'  # Include all fields or specify ['field1', 'field2']
