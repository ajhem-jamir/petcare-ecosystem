from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class AdoptionListing(models.Model):
    STATUS_CHOICES = (
        ('available', 'Available'),
        ('pending', 'Pending'),
        ('adopted', 'Adopted'),
        ('withdrawn', 'Withdrawn'),
    )
    
    SIZE_CHOICES = (
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large'),
        ('extra_large', 'Extra Large'),
    )
    
    AGE_GROUPS = (
        ('puppy_kitten', 'Puppy/Kitten'),
        ('young', 'Young'),
        ('adult', 'Adult'),
        ('senior', 'Senior'),
    )
    
    lister = models.ForeignKey(User, on_delete=models.CASCADE, related_name='adoption_listings')
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=50)
    breed = models.CharField(max_length=100, blank=True)
    age_group = models.CharField(max_length=15, choices=AGE_GROUPS)
    size = models.CharField(max_length=15, choices=SIZE_CHOICES)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')])
    color = models.CharField(max_length=100)
    description = models.TextField()
    personality_traits = models.TextField(help_text="Describe the pet's personality")
    medical_history = models.TextField(blank=True)
    is_vaccinated = models.BooleanField(default=False)
    is_spayed_neutered = models.BooleanField(default=False)
    is_house_trained = models.BooleanField(default=False)
    good_with_kids = models.BooleanField(default=False)
    good_with_pets = models.BooleanField(default=False)
    adoption_fee = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True, help_text="Adoption fee in Indian Rupees (₹)")
    location = models.CharField(max_length=200)
    contact_phone = models.CharField(max_length=15)
    contact_email = models.EmailField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='available')
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-featured', '-created_at']

    def __str__(self):
        return f"{self.name} - {self.species}"

class AdoptionPhoto(models.Model):
    listing = models.ForeignKey(AdoptionListing, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='adoption_photos/')
    caption = models.CharField(max_length=200, blank=True)
    is_primary = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Photo for {self.listing.name}"

class AdoptionApplication(models.Model):
    STATUS_CHOICES = (
        ('submitted', 'Submitted'),
        ('under_review', 'Under Review'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('withdrawn', 'Withdrawn'),
    )
    
    listing = models.ForeignKey(AdoptionListing, on_delete=models.CASCADE, related_name='applications')
    applicant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='adoption_applications')
    message = models.TextField(help_text="Why do you want to adopt this pet?")
    experience_with_pets = models.TextField()
    living_situation = models.TextField(help_text="Describe your living situation")
    other_pets = models.TextField(blank=True, help_text="Do you have other pets?")
    references = models.TextField(blank=True, help_text="Veterinary or personal references")
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='submitted')
    notes = models.TextField(blank=True, help_text="Internal notes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['listing', 'applicant']
        ordering = ['-created_at']

    def __str__(self):
        return f"Application for {self.listing.name} by {self.applicant.username}"