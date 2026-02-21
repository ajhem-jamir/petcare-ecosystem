from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Pet(models.Model):
    SPECIES_CHOICES = (
        ('dog', 'Dog'),
        ('cat', 'Cat'),
        ('bird', 'Bird'),
        ('rabbit', 'Rabbit'),
        ('fish', 'Fish'),
        ('other', 'Other'),
    )
    
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    
    ACTIVITY_CHOICES = (
        ('low', 'Low Activity'),
        ('medium', 'Medium Activity'),
        ('high', 'High Activity'),
    )
    
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pets')
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=10, choices=SPECIES_CHOICES)
    custom_species = models.CharField(max_length=100, blank=True, help_text="For species not in the list (admin only)")
    breed = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    birth_date = models.DateField()
    weight = models.DecimalField(max_digits=5, decimal_places=2, help_text="Weight in kg")
    activity_level = models.CharField(max_length=10, choices=ACTIVITY_CHOICES, default='medium', help_text="Pet's activity level")
    color = models.CharField(max_length=50, blank=True)
    microchip_id = models.CharField(max_length=50, blank=True, unique=True)
    photo = models.ImageField(upload_to='pets/', blank=True, null=True)
    medical_notes = models.TextField(blank=True)
    is_lost = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.owner.username})"
    
    def save(self, *args, **kwargs):
        """Override save to process image before saving"""
        # Check if auto-crop is enabled (can be disabled in settings)
        from django.conf import settings
        auto_crop_enabled = getattr(settings, 'PET_IMAGE_AUTO_CROP', True)
        
        # Only process new uploads, not existing images
        if self.photo and auto_crop_enabled:
            try:
                # Check if this is a new upload (has 'file' attribute)
                if hasattr(self.photo, 'file') and hasattr(self.photo.file, 'read'):
                    from .image_utils import process_pet_image
                    # Process the image (crop, resize, optimize)
                    self.photo = process_pet_image(self.photo)
            except Exception as e:
                # If processing fails, continue with original image
                print(f"Image processing error: {e}")
                import traceback
                traceback.print_exc()
        
        super().save(*args, **kwargs)
    
    def delete_old_photo(self):
        """Delete old photo file when replacing with new one"""
        if self.photo:
            import os
            if os.path.isfile(self.photo.path):
                os.remove(self.photo.path)

    def get_species_name(self):
        """Return custom species if set, otherwise return standard species"""
        if self.custom_species:
            return self.custom_species
        return self.get_species_display()

    @property
    def age_months(self):
        from datetime import date
        today = date.today()
        return (today.year - self.birth_date.year) * 12 + today.month - self.birth_date.month

class HealthRecord(models.Model):
    RECORD_TYPES = (
        ('vaccination', 'Vaccination'),
        ('checkup', 'Regular Checkup'),
        ('illness', 'Illness'),
        ('surgery', 'Surgery'),
        ('medication', 'Medication'),
    )
    
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='health_records')
    record_type = models.CharField(max_length=15, choices=RECORD_TYPES)
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    veterinarian = models.CharField(max_length=100, blank=True)
    cost = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True, help_text="Cost in Indian Rupees (₹)")
    next_due_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.pet.name} - {self.title}"

class FeedingSchedule(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='feeding_schedules')
    food_type = models.CharField(max_length=100)
    amount = models.CharField(max_length=50, help_text="e.g., 1 cup, 200g")
    time = models.TimeField()
    is_active = models.BooleanField(default=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['time']

    def __str__(self):
        return f"{self.pet.name} - {self.food_type} at {self.time}"

class DietRecommendation(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='diet_recommendations')
    calories = models.FloatField()
    protein = models.FloatField()
    fat = models.FloatField()
    carbs = models.FloatField()
    recommendation = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Diet for {self.pet.name}"