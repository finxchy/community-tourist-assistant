from django.shortcuts import render
from .models import Place

def home(request):
    places = Place.objects.all()
    return render(request, "home.html", {"places": places})
