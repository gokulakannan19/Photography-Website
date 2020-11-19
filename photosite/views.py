from django.shortcuts import render
from .models import Contact


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
    if request.method == "POST":
        bride_name = request.POST['bride_name']
        groom_name = request.POST['groom_name']
        email = request.POST['email']
        phone = request.POST['phone']
        referrals = request.POST['referrals']

        Contact.objects.create(bride_name=bride_name, groom_name=groom_name, email=email, phone=phone, referrals=referrals)
        return render(request, 'photosite/contact.html', {})
    else:
        return render(request, 'photosite/contact.html', {})



