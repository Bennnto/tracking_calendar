import calendar
from datetime import date
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponse
from .models import MyEvent
from django.template import loader
from .forms import EventForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def event_calendar(request, year=None, month=None):
    today = date.today()
    year = int(year) if year is not None else today.year
    month = int(month) if month is not None else today.month

    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = EventForm()

    events = MyEvent.objects.filter(date__year=year, date__month=month)
    events_by_day = {}
    for event in events:
        day = event.date.day
        events_by_day.setdefault(day, []).append(event)

    cal = calendar.Calendar(firstweekday=0)
    weeks = []
    week = []
    for d in cal.itermonthdays(year, month):
        week.append(d)
        if len(week) == 7:
            weeks.append(week)
            week = []
    if week:
        while len(week) < 7:
            week.append(0)
        weeks.append(week)
    month_name = calendar.month_name[month]

    context = {
        "form": form,
        "year": year,
        "month": month,
        "month_name": month_name,
        "weeks": weeks,
        "events_by_day": events_by_day,
    }
    template = loader.get_template('calendar.html')
    return HttpResponse(template.render(context, request))

@login_required(login_url='login')
def create_event(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_calendar')
    else:
        form = EventForm()

    today = date.today()
    year = today.year
    month = today.month
    events = MyEvent.objects.filter(date__year=year, date__month=month)
    events_by_day = {}
    for event in events:
        day = event.date.day
        events_by_day.setdefault(day, []).append(event)
    cal = calendar.Calendar(firstweekday=0)
    weeks = []
    week = []
    for d in cal.itermonthdays(year, month):
        week.append(d)
        if len(week) == 7:
            weeks.append(week)
            week = []
    if week:
        while len(week) < 7:
            week.append(0)
        weeks.append(week)
    month_name = calendar.month_name[month]

    template = loader.get_template('calendar.html')
    context = {
        'form': form,
        'year': year,
        'month': month,
        'month_name': month_name,
        'weeks': weeks,
        'events_by_day': events_by_day,
    }
    return HttpResponse(template.render(context, request))

def delete_event(request, id):
    content = get_object_or_404(MyEvent, id=id)
    content.delete()
    return redirect('event_calendar')
        

def event_detail(request, id):
    content = get_object_or_404(MyEvent, id=id)
    context = { 'content': content }
    template = loader.get_template('event_description.html')
    return HttpResponse(template.render(context, request))
