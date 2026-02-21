from rest_framework import generics, permissions
from .models import Appointment, VeterinaryClinic
from .serializers import AppointmentSerializer, VeterinaryClinicSerializer

class AppointmentListCreateView(generics.ListCreateAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Appointment.objects.filter(pet__owner=self.request.user)

class AppointmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Appointment.objects.filter(pet__owner=self.request.user)

class ClinicListView(generics.ListAPIView):
    queryset = VeterinaryClinic.objects.filter(is_active=True)
    serializer_class = VeterinaryClinicSerializer
    permission_classes = [permissions.IsAuthenticated]