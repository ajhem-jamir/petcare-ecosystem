from django.contrib import admin
from .models import Pet, HealthRecord, FeedingSchedule

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'species', 'breed', 'owner', 'age_months', 'is_lost')
    list_filter = ('species', 'gender', 'is_lost')
    search_fields = ('name', 'breed', 'owner__username', 'microchip_id')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(HealthRecord)
class HealthRecordAdmin(admin.ModelAdmin):
    list_display = ('pet', 'record_type', 'title', 'date', 'veterinarian')
    list_filter = ('record_type', 'date')
    search_fields = ('pet__name', 'title', 'veterinarian')

@admin.register(FeedingSchedule)
class FeedingScheduleAdmin(admin.ModelAdmin):
    list_display = ('pet', 'food_type', 'amount', 'time', 'is_active')
    list_filter = ('is_active', 'time')
    search_fields = ('pet__name', 'food_type')