from django.urls import path
from .views import home, add_place, place_detail

urlpatterns = [
    path("", home, name="home"),
    path("add/", add_place, name="add_place"),
    path("place/<int:place_id>/", place_detail, name="place_detail"),
]