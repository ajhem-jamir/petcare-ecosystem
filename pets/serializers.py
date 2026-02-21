from rest_framework import serializers
from .models import Pet, HealthRecord, FeedingSchedule

class PetSerializer(serializers.ModelSerializer):
    age_months = serializers.ReadOnlyField()
    
    class Meta:
        model = Pet
        fields = ['id', 'name', 'species', 'breed', 'gender', 'birth_date', 
                 'weight', 'color', 'microchip_id', 'photo', 'medical_notes', 
                 'age_months', 'created_at']
        read_only_fields = ['id', 'created_at']

class HealthRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthRecord
        fields = ['id', 'record_type', 'title', 'description', 'date', 
                 'veterinarian', 'cost', 'next_due_date', 'created_at']
        read_only_fields = ['id', 'created_at']

class FeedingScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedingSchedule
        fields = ['id', 'food_type', 'amount', 'time', 'is_active', 'notes']
        read_only_fields = ['id']