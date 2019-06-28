from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def home_page(request):
    return HttpResponse('<html><title>Meet My Peeps</title></html>')
