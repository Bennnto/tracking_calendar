from django.urls import path
from . import views

urlpatterns = [
    path('calendar/', views.event_calendar, name='event_calendar'),
    path('calendar/create/', views.create_event, name='create_event'),
    path('calendar/del/<int:id>/', views.delete_event, name='delete_event'),
    path('calendar/info/<int:id>/', views.event_detail, name='event_detail')
]