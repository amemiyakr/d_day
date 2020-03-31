from rest_framework import serializers
from event_management.models import Menu


class Serializers(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('id', 'title')
