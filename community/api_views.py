from rest_framework import generics, permissions
from .models import ForumPost, LostPetReport
from .serializers import ForumPostSerializer, LostPetReportSerializer

class ForumPostListView(generics.ListAPIView):
    queryset = ForumPost.objects.all()
    serializer_class = ForumPostSerializer
    permission_classes = [permissions.IsAuthenticated]

class LostPetReportListView(generics.ListAPIView):
    queryset = LostPetReport.objects.filter(is_active=True)
    serializer_class = LostPetReportSerializer
    permission_classes = [permissions.IsAuthenticated]