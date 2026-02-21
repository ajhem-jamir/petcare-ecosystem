from django.urls import path
from . import api_views

urlpatterns = [
    path('', api_views.AdoptionListingListView.as_view(), name='adoption-listing-list'),
    path('<int:pk>/', api_views.AdoptionListingDetailView.as_view(), name='adoption-listing-detail'),
    path('applications/', api_views.AdoptionApplicationListView.as_view(), name='adoption-application-list'),
]