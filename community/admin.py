from django.contrib import admin
from .models import ForumCategory, ForumPost, ForumReply, LostPetReport

@admin.register(ForumCategory)
class ForumCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'created_at')
    list_filter = ('is_active',)

@admin.register(ForumPost)
class ForumPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'post_type', 'is_pinned', 'created_at')
    list_filter = ('post_type', 'category', 'is_pinned', 'is_solved')
    search_fields = ('title', 'content', 'author__username')

@admin.register(LostPetReport)
class LostPetReportAdmin(admin.ModelAdmin):
    list_display = ('pet_name', 'species', 'status', 'last_seen_date', 'reporter', 'reward_amount_display')
    list_filter = ('status', 'species', 'size', 'last_seen_date')
    search_fields = ('pet_name', 'description', 'last_seen_location', 'reporter__username')
    readonly_fields = ('created_at', 'updated_at')
    list_editable = ('status',)
    
    def reward_amount_display(self, obj):
        if obj.reward_amount:
            return f"₹{obj.reward_amount}"
        return "No reward"
    reward_amount_display.short_description = "Reward Amount"