from django import forms
from .models import AdoptionListing, AdoptionApplication, AdoptionPhoto

class AdoptionListingForm(forms.ModelForm):
    class Meta:
        model = AdoptionListing
        fields = [
            'name', 'species', 'breed', 'age_group', 'size', 'gender', 'color',
            'description', 'personality_traits', 'medical_history', 'is_vaccinated',
            'is_spayed_neutered', 'is_house_trained', 'good_with_kids', 'good_with_pets',
            'adoption_fee', 'location', 'contact_phone', 'contact_email'
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'personality_traits': forms.Textarea(attrs={'rows': 3}),
            'medical_history': forms.Textarea(attrs={'rows': 3}),
        }
        labels = {
            'adoption_fee': 'Adoption Fee (₹)',
        }
        help_texts = {
            'adoption_fee': 'Enter amount in Indian Rupees (₹). Leave blank for free adoption.',
        }

class AdoptionPhotoForm(forms.ModelForm):
    class Meta:
        model = AdoptionPhoto
        fields = ['image', 'caption', 'is_primary']

class AdoptionApplicationForm(forms.ModelForm):
    class Meta:
        model = AdoptionApplication
        fields = [
            'message', 'experience_with_pets', 'living_situation', 
            'other_pets', 'references'
        ]
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Tell us why you want to adopt this pet...'}),
            'experience_with_pets': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Describe your experience with pets...'}),
            'living_situation': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Describe your home, yard, living arrangements...'}),
            'other_pets': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Do you have other pets? Tell us about them...'}),
            'references': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Veterinary references or personal references...'}),
        }