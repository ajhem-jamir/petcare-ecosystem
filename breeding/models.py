from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class BreederListing(models.Model):
    VERIFICATION_STATUS = (
        ('pending', 'Pending Verification'),
        ('verified', 'Verified'),
        ('rejected', 'Rejected'),
    )
    
    breeder = models.ForeignKey(User, on_delete=models.CASCADE, related_name='breeder_listings')
    business_name = models.CharField(max_length=200)
    license_number = models.CharField(max_length=100, blank=True, help_text="Breeding license number")
    species_specialization = models.CharField(max_length=100, help_text="e.g., Dogs, Cats, Birds")
    breeds_available = models.TextField(help_text="List of breeds you specialize in")
    location = models.CharField(max_length=200)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    website = models.URLField(blank=True)
    description = models.TextField(help_text="About your breeding program")
    experience_years = models.PositiveIntegerField(help_text="Years of breeding experience")
    health_testing = models.BooleanField(default=False, help_text="Do you conduct health testing?")
    health_guarantee = models.BooleanField(default=False, help_text="Do you provide health guarantee?")
    certifications = models.TextField(blank=True, help_text="Professional certifications and memberships")
    photo = models.ImageField(upload_to='breeders/', blank=True, help_text="Business or facility photo")
    verification_status = models.CharField(max_length=10, choices=VERIFICATION_STATUS, default='pending')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-verification_status', '-created_at']

    def __str__(self):
        return f"{self.business_name} - {self.species_specialization}"

    @property
    def average_rating(self):
        reviews = self.reviews.all()
        if reviews:
            return sum(review.rating for review in reviews) / len(reviews)
        return 0

class BreederReview(models.Model):
    RATING_CHOICES = (
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    )
    
    breeder = models.ForeignKey(BreederListing, on_delete=models.CASCADE, related_name='reviews')
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='breeder_reviews')
    rating = models.IntegerField(choices=RATING_CHOICES)
    title = models.CharField(max_length=200)
    review_text = models.TextField()
    purchase_date = models.DateField(blank=True, null=True)
    would_recommend = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['breeder', 'reviewer']
        ordering = ['-created_at']

    def __str__(self):
        return f"Review for {self.breeder.business_name} by {self.reviewer.username}"