from rest_framework import serializers
from event_management.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventUser
        fields = '__all__'


class EventDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = EventDay
        fields = '__all__'
