from django.urls import path
from .views import diet_recommendation_view

urlpatterns = [
    path("recommend/<int:pet_id>/", diet_recommendation_view, name="diet_recommendation"),
]