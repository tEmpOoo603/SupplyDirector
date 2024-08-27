from django.contrib import admin

from main.models import Events, EventsChanges


@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'start_at', 'period']
    search_fields = ['name','id']

@admin.register(EventsChanges)
class EventsChangesAdmin(admin.ModelAdmin):
    list_display = ['id','event', 'name', 'status', 'updated']
    search_fields = ['name','id']
