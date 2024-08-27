from datetime import datetime, timedelta

import pytz
from django.shortcuts import render
from rest_framework.generics import *
from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializers import EventsSerializer, EventsReadSerializer, EventsChangesSerializer
from main.models import Events, EventsChanges
from pytz import timezone


class BaseEventsAPI(CreateAPIView):
    def create_event(self, status, name=None):
        data = self.kwargs.copy()
        if name:
            data['name'] = name
        data['event'] = self.kwargs['id']
        data['status'] = status
        data['updated'] = datetime(self.kwargs.get('year'), self.kwargs.get('month'), self.kwargs.get('day'))
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({'id': self.kwargs['id']})


class EventsAPICreate(CreateAPIView):
    serializer_class = EventsSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({'id': serializer.data.get('id')})


class EventsAPIRemove(BaseEventsAPI):
    serializer_class = EventsChangesSerializer

    def create(self, request, *args, **kwargs):
        return self.create_event('STOP')


class EventsAPIRemoveAll(BaseEventsAPI):
    serializer_class = EventsChangesSerializer

    def create(self, request, *args, **kwargs):
        return self.create_event('DELETE')


class EventsAPIUpdate(BaseEventsAPI):
    serializer_class = EventsChangesSerializer

    def create(self, request, *args, **kwargs):
        name = request.data.get('name')
        if not name:
            return Response({'error':'Поле name - обязательно'})
        return self.create_event('RENAME', name=name)


class EventsAPIList(ListAPIView):
    serializer_class = EventsReadSerializer

    def get_queryset(self):
        new_tz = timezone('Europe/Moscow')
        all_events = Events.objects.prefetch_related('events').all()
        day_filter = datetime(self.kwargs.get('year'), self.kwargs.get('month'), self.kwargs.get('day'))
        day_filter_date = day_filter.date()
        day_filter_updated = day_filter.replace()
        q = []
        for event in all_events:
            event_start = event.start_at.astimezone(new_tz)
            event_start_date = event_start.date()
            if ((event.period is not None
                 and event_start_date < day_filter_date
                 and int((day_filter_date - event_start_date).days) % event.period == 0)
                    or event_start_date == day_filter_date):
                changes = event.events
                if changes:
                    for change in event.events.all():
                        change_date = change.updated.astimezone(new_tz)
                        if ((change.status == 'STOP' and change_date.date() == day_filter_date)
                                or (change.status == 'DELETE' and day_filter_date >= change_date.date())):
                            break
                        elif change.status == 'RENAME' and day_filter_date == change_date.date():
                                day_filter_updated = change_date
                                event.name = change.name
                    else:
                        q.append(event)
                else:
                    q.append(event)
        return q
