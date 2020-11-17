from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('home/', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('wedding/', views.wedding, name="wedding"),
    path('commercial/', views.commercial, name="commercial"),
    path('film/', views.film, name="film"),
    path('contact/', views.contact, name="contact"),
]