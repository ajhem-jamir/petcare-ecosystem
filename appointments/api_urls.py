from django.urls import path
from . import api_views

urlpatterns = [
    path('', api_views.AppointmentListCreateView.as_view(), name='appointment-list-create'),
    path('<int:pk>/', api_views.AppointmentDetailView.as_view(), name='appointment-detail'),
    path('clinics/', api_views.ClinicListView.as_view(), name='clinic-list'),
]