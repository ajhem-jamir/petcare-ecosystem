from django.contrib import admin
from .models import VeterinaryClinic, Appointment, AppointmentReminder

@admin.register(VeterinaryClinic)
class VeterinaryClinicAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'phone', 'email')

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('pet', 'clinic', 'appointment_type', 'date', 'time', 'status')
    list_filter = ('status', 'appointment_type', 'date')
    search_fields = ('pet__name', 'clinic__name', 'veterinarian')

@admin.register(AppointmentReminder)
class AppointmentReminderAdmin(admin.ModelAdmin):
    list_display = ('appointment', 'reminder_type', 'send_time', 'is_sent')
    list_filter = ('reminder_type', 'is_sent')