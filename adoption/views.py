from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import AdoptionListing, AdoptionApplication, AdoptionPhoto
from .forms import AdoptionListingForm, AdoptionApplicationForm, AdoptionPhotoForm

def adoption_list(request):
    search_query = request.GET.get('search', '')
    species_filter = request.GET.get('species', '')
    age_filter = request.GET.get('age', '')
    
    listings = AdoptionListing.objects.filter(status='available')
    
    if species_filter:
        listings = listings.filter(species__icontains=species_filter)
    
    if age_filter:
        listings = listings.filter(age_group=age_filter)
    
    if search_query:
        listings = listings.filter(
            Q(name__icontains=search_query) |
            Q(breed__icontains=search_query) |
            Q(location__icontains=search_query) |
            Q(description__icontains=search_query)
        )
    
    return render(request, 'adoption/adoption_list.html', {
        'listings': listings,
        'search_query': search_query,
        'species_filter': species_filter,
        'age_filter': age_filter
    })

def adoption_detail(request, listing_id):
    listing = get_object_or_404(AdoptionListing, id=listing_id)
    user_application = None
    
    if request.user.is_authenticated:
        user_application = AdoptionApplication.objects.filter(
            listing=listing, applicant=request.user
        ).first()
    
    return render(request, 'adoption/adoption_detail.html', {
        'listing': listing,
        'user_application': user_application
    })

@login_required
def apply_for_adoption(request, listing_id):
    listing = get_object_or_404(AdoptionListing, id=listing_id, status='available')
    
    # Check if user already applied
    existing_application = AdoptionApplication.objects.filter(
        listing=listing, applicant=request.user
    ).first()
    
    if existing_application:
        messages.warning(request, 'You have already applied for this pet.')
        return redirect('adoption:adoption_detail', listing_id=listing.id)
    
    if request.method == 'POST':
        form = AdoptionApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.listing = listing
            application.applicant = request.user
            application.save()
            messages.success(request, f'Your application for {listing.name} has been submitted!')
            return redirect('adoption:adoption_detail', listing_id=listing.id)
    else:
        form = AdoptionApplicationForm()
    
    return render(request, 'adoption/apply_for_adoption.html', {
        'form': form,
        'listing': listing
    })

@login_required
def create_listing(request):
    if request.method == 'POST':
        form = AdoptionListingForm(request.POST)
        photo_form = AdoptionPhotoForm(request.POST, request.FILES)
        
        if form.is_valid() and photo_form.is_valid():
            listing = form.save(commit=False)
            listing.lister = request.user
            listing.save()
            
            if photo_form.cleaned_data['image']:
                photo = photo_form.save(commit=False)
                photo.listing = listing
                photo.is_primary = True
                photo.save()
            
            messages.success(request, f'Adoption listing for {listing.name} has been created!')
            return redirect('adoption:adoption_detail', listing_id=listing.id)
    else:
        form = AdoptionListingForm()
        photo_form = AdoptionPhotoForm()
    
    return render(request, 'adoption/create_listing.html', {
        'form': form,
        'photo_form': photo_form
    })

@login_required
def my_applications(request):
    applications = AdoptionApplication.objects.filter(applicant=request.user)
    return render(request, 'adoption/my_applications.html', {
        'applications': applications
    })