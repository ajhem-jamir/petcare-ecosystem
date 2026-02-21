from django.urls import path, include

urlpatterns = [
    path('pets/', include('pets.api_urls')),
    path('appointments/', include('appointments.api_urls')),
    path('community/', include('community.api_urls')),
    path('adoption/', include('adoption.api_urls')),
]