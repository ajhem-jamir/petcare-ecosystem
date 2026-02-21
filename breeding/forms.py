from django import forms
from .models import BreederListing, BreederReview

class BreederListingForm(forms.ModelForm):
    class Meta:
        model = BreederListing
        fields = [
            'business_name', 'species_specialization', 'breeds_available',
            'location', 'address', 'phone', 'email', 'website', 'description',
            'experience_years', 'health_testing', 'health_guarantee', 'certifications', 'photo'
        ]
        widgets = {
            'breeds_available': forms.Textarea(attrs={'rows': 3}),
            'address': forms.Textarea(attrs={'rows': 3}),
            'description': forms.Textarea(attrs={'rows': 4}),
            'certifications': forms.Textarea(attrs={'rows': 3}),
        }

class BreederReviewForm(forms.ModelForm):
    class Meta:
        model = BreederReview
        fields = ['rating', 'title', 'review_text', 'purchase_date', 'would_recommend']
        widgets = {
            'purchase_date': forms.DateInput(attrs={'type': 'date'}),
            'review_text': forms.Textarea(attrs={'rows': 4}),
        }