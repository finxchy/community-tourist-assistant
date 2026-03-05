from django.shortcuts import redirect, render, get_object_or_404
from .models import Place
from .form import PlaceForm

def home(request):
    places = Place.objects.all()
    return render(request, "home.html", {"places": places})

def add_place(request):
    if request.method == "POST":
        form = PlaceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = PlaceForm()
    return render(request, "add_place.html", {"form": form})

def place_detail(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    return render(request, "place_detail.html", {"place": place})