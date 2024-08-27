from rest_framework import serializers

from main.models import Events, EventsChanges


class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'


class EventsReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ['name', 'id', 'start_at']


class EventsChangesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventsChanges
        fields = '__all__'
