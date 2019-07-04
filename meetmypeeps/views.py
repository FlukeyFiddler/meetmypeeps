from django.shortcuts import render
from django.utils.dateparse import parse_datetime
from django.utils.timezone import make_aware
from meetmypeeps.models import Event
from django.contrib.gis.geos import Point


def home_page(request):
    event = Event()
    event.title = request.POST.get('title', '')
    point = request.POST.get('loc', '0,0').split(',')
    event.location = Point(float(point[0]), float(point[1]))
    event.date = make_aware(parse_datetime(request.POST.get('date', '')))
    event.save()

    return render(request, 'home.html', {
        'title': request.POST.get('title', ''),
        'loc': request.POST.get('loc', ''),
        'date': request.POST.get('date', ''),
    })
