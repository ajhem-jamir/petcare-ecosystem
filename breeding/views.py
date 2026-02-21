from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import BreederListing, BreederReview
from .forms import BreederListingForm, BreederReviewForm

def breeder_list(request):
    search_query = request.GET.get('search', '')
    species_filter = request.GET.get('species', '')
    
    breeders = BreederListing.objects.filter(is_active=True, verification_status='verified')
    
    if species_filter:
        breeders = breeders.filter(species_specialization__icontains=species_filter)
    
    if search_query:
        breeders = breeders.filter(
            Q(business_name__icontains=search_query) |
            Q(breeds_available__icontains=search_query) |
            Q(location__icontains=search_query)
        )
    
    return render(request, 'breeding/breeder_list.html', {
        'breeders': breeders,
        'search_query': search_query,
        'species_filter': species_filter
    })

def breeder_detail(request, breeder_id):
    breeder = get_object_or_404(BreederListing, id=breeder_id, is_active=True)
    reviews = breeder.reviews.all()[:10]
    return render(request, 'breeding/breeder_detail.html', {
        'breeder': breeder,
        'reviews': reviews
    })

@login_required
def create_breeder_listing(request):
    if request.method == 'POST':
        form = BreederListingForm(request.POST, request.FILES)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.breeder = request.user
            listing.save()
            messages.success(request, 'Breeder listing created! It will be reviewed before going live.')
            return redirect('breeding:breeder_list')
    else:
        form = BreederListingForm()
    return render(request, 'breeding/create_listing.html', {'form': form})

@login_required
def add_review(request, breeder_id):
    breeder = get_object_or_404(BreederListing, id=breeder_id, is_active=True)
    
    # Check if user already reviewed this breeder
    existing_review = BreederReview.objects.filter(breeder=breeder, reviewer=request.user).first()
    if existing_review:
        messages.warning(request, 'You have already reviewed this breeder.')
        return redirect('breeding:breeder_detail', breeder_id=breeder.id)
    
    if request.method == 'POST':
        form = BreederReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.breeder = breeder
            review.reviewer = request.user
            review.save()
            messages.success(request, 'Review added successfully!')
            return redirect('breeding:breeder_detail', breeder_id=breeder.id)
    else:
        form = BreederReviewForm()
    
    return render(request, 'breeding/add_review.html', {
        'form': form,
        'breeder': breeder
    })