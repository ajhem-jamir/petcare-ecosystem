from django.urls import path
from . import api_views

urlpatterns = [
    path('posts/', api_views.ForumPostListView.as_view(), name='forum-post-list'),
    path('lost-pets/', api_views.LostPetReportListView.as_view(), name='lost-pet-list'),
]