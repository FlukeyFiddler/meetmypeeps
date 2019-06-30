from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def home_page(request):
    return render(request, 'home.html', {
        'title': request.POST.get('title', ''),
        'lat': request.POST.get('lat', ''),
        'lon': request.POST.get('lon', ''),
        'date': request.POST.get('date', ''),
    })
