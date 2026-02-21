from django.contrib import admin
from .models import BreederListing, BreederReview

@admin.register(BreederListing)
class BreederListingAdmin(admin.ModelAdmin):
    list_display = ('business_name', 'species_specialization', 'location', 'verification_status', 'is_active', 'created_at')
    list_filter = ('verification_status', 'species_specialization', 'health_testing', 'health_guarantee')
    search_fields = ('business_name', 'breeds_available', 'location', 'breeder__username')
    list_editable = ('verification_status', 'is_active')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(BreederReview)
class BreederReviewAdmin(admin.ModelAdmin):
    list_display = ('breeder', 'reviewer', 'rating', 'title', 'would_recommend', 'created_at')
    list_filter = ('rating', 'would_recommend', 'created_at')
    search_fields = ('breeder__business_name', 'reviewer__username', 'title')