from django.db import models
from django.contrib.auth import get_user_model
from pets.models import Pet

User = get_user_model()

class VeterinaryClinic(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    website = models.URLField(blank=True)
    services = models.TextField(help_text="List of services offered")
    operating_hours = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    STATUS_CHOICES = (
        ('scheduled', 'Scheduled'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
        ('no_show', 'No Show'),
    )
    
    APPOINTMENT_TYPES = (
        ('checkup', 'Regular Checkup'),
        ('vaccination', 'Vaccination'),
        ('emergency', 'Emergency'),
        ('surgery', 'Surgery'),
        ('grooming', 'Grooming'),
        ('consultation', 'Consultation'),
    )
    
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='appointments')
    clinic = models.ForeignKey(VeterinaryClinic, on_delete=models.CASCADE, related_name='appointments')
    appointment_type = models.CharField(max_length=15, choices=APPOINTMENT_TYPES)
    date = models.DateField()
    time = models.TimeField()
    duration = models.DurationField(help_text="Expected duration")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='scheduled')
    notes = models.TextField(blank=True, help_text="Special instructions or notes")
    veterinarian = models.CharField(max_length=100, blank=True)
    cost = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True, help_text="Cost in Indian Rupees (₹)")
    reminder_sent = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['date', 'time']
        unique_together = ['clinic', 'date', 'time']

    def __str__(self):
        return f"{self.pet.name} - {self.appointment_type} on {self.date}"

class AppointmentReminder(models.Model):
    REMINDER_TYPES = (
        ('email', 'Email'),
        ('sms', 'SMS'),
        ('push', 'Push Notification'),
    )
    
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='reminders')
    reminder_type = models.CharField(max_length=5, choices=REMINDER_TYPES)
    send_time = models.DateTimeField()
    is_sent = models.BooleanField(default=False)
    sent_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.appointment} - {self.reminder_type} reminder"