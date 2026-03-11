from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("add/", views.add_place, name="add_place"),
    path("place/<int:pk>/", views.place_detail, name="place_detail"),
    path("place/<int:pk>/review/", views.add_review, name="add_review"),
]