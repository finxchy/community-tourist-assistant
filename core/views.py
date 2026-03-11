from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Place
from .form import PlaceForm, ReviewForm

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

def place_detail(request, pk):
    place = get_object_or_404(Place, pk=pk)
    form = ReviewForm()
    return render(request, "place_detail.html", {
        "place": place,
        "form": form,
    })

@login_required
def add_review(request, pk):
    place = get_object_or_404(Place, pk=pk)

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.place = place
            review.user = request.user
            review.save()
            return redirect("place_detail", pk=place.pk)

    return redirect("place_detail", pk=place.pk)