from django import forms
from .models import Place, Review

class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ["name", "description", "town", "image_filename"]

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["rating", "comment"]