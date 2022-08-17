from django.urls import path

from . import views

urlpatterns = [
    path("animals/<animal_id>/", views.AnimalDetailView.as_view()),
    path("animals/", views.AnimalView.as_view()),
]
