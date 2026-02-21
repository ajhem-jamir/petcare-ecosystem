from django.urls import path
from . import views

app_name = 'pets'

urlpatterns = [
    path('', views.pet_list, name='pet_list'),
    path('<int:pet_id>/', views.pet_detail, name='pet_detail'),
    path('add/', views.add_pet, name='add_pet'),
    path('<int:pet_id>/edit/', views.edit_pet, name='edit_pet'),
    path('<int:pet_id>/health/add/', views.add_health_record, name='add_health_record'),
    path('<int:pet_id>/diet/', views.diet_recommendation, name='diet_recommendation'),
    path('<int:pet_id>/ai-recommendations/', views.ai_pet_recommendations, name='ai_recommendations'),
]