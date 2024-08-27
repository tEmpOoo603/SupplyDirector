from django.urls import path

from api.views import *

app_name = 'api'

urlpatterns = [
    path('add/', EventsAPICreate.as_view()),
    path('remove/<int:id>/<int:year>/<int:month>/<int:day>/', EventsAPIRemove.as_view()),
    path('remove-next/<int:id>/<int:year>/<int:month>/<int:day>/', EventsAPIRemoveAll.as_view()),
    path('update/<int:id>/<int:year>/<int:month>/<int:day>/', EventsAPIUpdate.as_view()),
    path('events/<int:year>/<int:month>/<int:day>/', EventsAPIList.as_view()),

]