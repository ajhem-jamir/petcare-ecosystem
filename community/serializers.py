from rest_framework import serializers
from .models import ForumPost, LostPetReport, ForumCategory

class ForumCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumCategory
        fields = ['id', 'name', 'description', 'icon']

class ForumPostSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source='author.username', read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)
    
    class Meta:
        model = ForumPost
        fields = ['id', 'title', 'content', 'post_type', 'author_username', 
                 'category_name', 'views_count', 'is_solved', 'created_at']

class LostPetReportSerializer(serializers.ModelSerializer):
    reporter_username = serializers.CharField(source='reporter.username', read_only=True)
    
    class Meta:
        model = LostPetReport
        fields = ['id', 'pet_name', 'species', 'breed', 'color', 'size', 
                 'last_seen_location', 'last_seen_date', 'description', 
                 'contact_phone', 'status', 'reporter_username', 'created_at']