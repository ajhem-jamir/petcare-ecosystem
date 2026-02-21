from rest_framework import generics, permissions
from .models import AdoptionListing, AdoptionApplication
from .serializers import AdoptionListingSerializer, AdoptionApplicationSerializer

class AdoptionListingListView(generics.ListAPIView):
    queryset = AdoptionListing.objects.filter(status='available')
    serializer_class = AdoptionListingSerializer
    permission_classes = [permissions.IsAuthenticated]

class AdoptionListingDetailView(generics.RetrieveAPIView):
    queryset = AdoptionListing.objects.all()
    serializer_class = AdoptionListingSerializer
    permission_classes = [permissions.IsAuthenticated]

class AdoptionApplicationListView(generics.ListCreateAPIView):
    serializer_class = AdoptionApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return AdoptionApplication.objects.filter(applicant=self.request.user)