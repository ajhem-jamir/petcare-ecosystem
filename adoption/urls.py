from django.urls import path
from . import views

app_name = 'adoption'

urlpatterns = [
    path('', views.adoption_list, name='adoption_list'),
    path('<int:listing_id>/', views.adoption_detail, name='adoption_detail'),
    path('<int:listing_id>/apply/', views.apply_for_adoption, name='apply_for_adoption'),
    path('create/', views.create_listing, name='create_listing'),
    path('my-applications/', views.my_applications, name='my_applications'),
]