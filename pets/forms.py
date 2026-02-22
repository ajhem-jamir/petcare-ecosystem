from django import forms
from .models import Pet, HealthRecord, FeedingSchedule

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'species', 'custom_species', 'breed', 'gender', 'birth_date', 'weight', 'activity_level', 'color', 'microchip_id', 'photo', 'medical_notes']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
            'medical_notes': forms.Textarea(attrs={'rows': 4}),
        }
        help_texts = {
            'custom_species': 'Only fill this if species is "Other" and you want to specify (e.g., Hamster, Ferret, Iguana)',
            'photo': 'Upload a photo (max 5MB). Image will be automatically cropped to square and optimized.',
            'microchip_id': 'Optional - Enter microchip number if your pet has one',
        }
    
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        
        # Only show custom_species field to admin/superuser
        if self.user and not (self.user.is_staff or self.user.is_superuser):
            self.fields['custom_species'].widget = forms.HiddenInput()
            self.fields['custom_species'].required = False
    
    def clean_photo(self):
        """Validate uploaded photo"""
        photo = self.cleaned_data.get('photo')
        
        if photo:
            from .image_utils import validate_image
            
            # Validate image
            is_valid, error_message = validate_image(photo)
            if not is_valid:
                raise forms.ValidationError(error_message)
        
        return photo

class HealthRecordForm(forms.ModelForm):
    class Meta:
        model = HealthRecord
        fields = ['record_type', 'title', 'description', 'date', 'veterinarian', 'cost', 'next_due_date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'next_due_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 4}),
        }

class FeedingScheduleForm(forms.ModelForm):
    class Meta:
        model = FeedingSchedule
        fields = ['food_type', 'amount', 'time', 'notes']
        widgets = {
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'notes': forms.Textarea(attrs={'rows': 3}),
        }