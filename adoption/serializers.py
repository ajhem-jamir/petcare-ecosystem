from rest_framework import serializers
from .models import AdoptionListing, AdoptionApplication

class AdoptionListingSerializer(serializers.ModelSerializer):
    lister_username = serializers.CharField(source='lister.username', read_only=True)
    
    class Meta:
        model = AdoptionListing
        fields = ['id', 'name', 'species', 'breed', 'age_group', 'size', 'gender', 
                 'color', 'description', 'personality_traits', 'is_vaccinated', 
                 'is_spayed_neutered', 'adoption_fee', 'location', 'contact_phone', 
                 'contact_email', 'lister_username', 'created_at']

class AdoptionApplicationSerializer(serializers.ModelSerializer):
    listing_name = serializers.CharField(source='listing.name', read_only=True)
    
    class Meta:
        model = AdoptionApplication
        fields = ['id', 'listing', 'listing_name', 'message', 'experience_with_pets', 
                 'living_situation', 'other_pets', 'references', 'status', 'created_at']
        read_only_fields = ['id', 'status', 'created_at']