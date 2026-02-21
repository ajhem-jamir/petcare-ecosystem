from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.forum_list, name='forum_list'),
    path('category/<int:category_id>/', views.category_posts, name='category_posts'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('create/', views.create_post, name='create_post'),
    path('lost-pets/', views.lost_pets, name='lost_pets'),
    path('lost-pets/report/', views.report_lost_pet, name='report_lost_pet'),
    path('lost-pets/<int:report_id>/', views.lost_pet_detail, name='lost_pet_detail'),
]