from django.shortcuts import render, redirect
from django.utils.dateparse import parse_datetime
from django.utils.timezone import make_aware
from meetmypeeps.models import Event
from django.contrib.gis.geos import Point


def home_page(request):
    show_own_events = False
    event = Event()
    if request.method == 'POST':
        event.title = request.POST.get('title', '')
        point = request.POST.get('loc', '0,0').split(',')
        event.location = Point(float(point[0]), float(point[1]))
        event.date = make_aware(parse_datetime(request.POST.get('date', '2999-01-01 00:00')))
        event.save()

        return redirect('/')

    return render(request, 'home.html')
    '''
        , {
        'show_own_events': show_own_events,
        'title': event.title,
        'loc': f'{event.location.x}, {event.location.y}',
        'date': event.date.strftime('%Y-%m-%d %H:%M'),
    })
    '''
