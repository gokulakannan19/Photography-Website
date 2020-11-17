from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'index.html', {})


def home(request):
    return render(request, 'photosite/home.html', {})


def about(request):
    return render(request, 'photosite/about.html', {})


def film(request):
    return render(request, 'photosite/film.html', {})


def commercial(request):
    return render(request, 'photosite/commercial.html', {})


def wedding(request):
    return render(request, 'photosite/wedding.html', {})


def contact(request):
    return render(request, 'photosite/contact.html', {})
