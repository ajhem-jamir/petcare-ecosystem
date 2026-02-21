from rest_framework import serializers
from .models import Appointment, VeterinaryClinic

class VeterinaryClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = VeterinaryClinic
        fields = ['id', 'name', 'address', 'phone', 'email', 'website', 'services', 'operating_hours']

class AppointmentSerializer(serializers.ModelSerializer):
    clinic_name = serializers.CharField(source='clinic.name', read_only=True)
    pet_name = serializers.CharField(source='pet.name', read_only=True)
    
    class Meta:
        model = Appointment
        fields = ['id', 'pet', 'pet_name', 'clinic', 'clinic_name', 'appointment_type', 
                 'date', 'time', 'status', 'notes', 'veterinarian', 'cost']
        read_only_fields = ['id']