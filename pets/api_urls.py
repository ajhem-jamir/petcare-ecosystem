from django.urls import path
from . import api_views

urlpatterns = [
    path('', api_views.PetListCreateView.as_view(), name='pet-list-create'),
    path('<int:pk>/', api_views.PetDetailView.as_view(), name='pet-detail'),
    path('<int:pet_id>/health/', api_views.HealthRecordListCreateView.as_view(), name='health-record-list'),
]