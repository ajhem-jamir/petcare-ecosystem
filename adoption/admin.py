from django.contrib import admin
from .models import AdoptionListing, AdoptionPhoto, AdoptionApplication

@admin.register(AdoptionListing)
class AdoptionListingAdmin(admin.ModelAdmin):
    list_display = ('name', 'species', 'breed', 'lister', 'status', 'featured', 'created_at')
    list_filter = ('status', 'species', 'age_group', 'size', 'featured')
    search_fields = ('name', 'breed', 'description', 'lister__username')
    list_editable = ('featured', 'status')

@admin.register(AdoptionApplication)
class AdoptionApplicationAdmin(admin.ModelAdmin):
    list_display = ('listing', 'applicant', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('listing__name', 'applicant__username', 'message')