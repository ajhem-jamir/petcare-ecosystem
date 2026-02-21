from django.urls import path
from . import views

app_name = 'breeding'

urlpatterns = [
    path('', views.breeder_list, name='breeder_list'),
    path('<int:breeder_id>/', views.breeder_detail, name='breeder_detail'),
    path('create/', views.create_breeder_listing, name='create_listing'),
    path('<int:breeder_id>/review/', views.add_review, name='add_review'),
]