from django.db import models
from django.db.models import CASCADE
from django.core.exceptions import ValidationError


class Events(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False)
    start_at = models.DateTimeField(null=False, blank=False)
    period = models.IntegerField(default=None, blank=True, null=True)

    class Meta:
        db_table = 'events'
        verbose_name = 'Событие'
        verbose_name_plural = 'События'

    def __str__(self):
        return self.name


class EventsChanges(models.Model):
    CHOICES = [
        ("RENAME", 'Rename'),
        ("STOP", 'Stop'),
        ("DELETE", 'Delete'),
    ]

    event = models.ForeignKey(to=Events, related_name='events', on_delete=CASCADE)
    status = models.CharField(max_length=20, choices=CHOICES, blank=False)
    name = models.CharField(max_length=128, blank=True)
    updated = models.DateTimeField()

    def clean(self):
        super().clean()
        if self.status == 'RENAME' and not self.name:
            raise ValidationError({'name':'Поле "name" обязательно, если выбрано status=RENAME'})

    class Meta:
        db_table = 'events_changes'
        verbose_name = 'Изменение События'
        verbose_name_plural = 'Изменения События'