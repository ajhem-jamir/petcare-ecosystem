from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from appointments.models import VeterinaryClinic
from community.models import ForumCategory
from datetime import date

User = get_user_model()

class Command(BaseCommand):
    help = 'Populate database with sample data for development'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample data...')
        
        # Create sample veterinary clinics
        clinics_data = [
            {
                'name': 'Happy Paws Veterinary Clinic',
                'address': '123 Main Street, City Center',
                'phone': '+1-555-0123',
                'email': 'info@happypaws.com',
                'services': 'General checkups, Vaccinations, Surgery, Emergency care',
                'operating_hours': 'Mon-Fri: 8AM-6PM, Sat: 9AM-4PM, Sun: Closed'
            },
            {
                'name': 'Pet Care Plus',
                'address': '456 Oak Avenue, Downtown',
                'phone': '+1-555-0456',
                'email': 'contact@petcareplus.com',
                'services': 'Dental care, Grooming, Boarding, Wellness exams',
                'operating_hours': 'Mon-Sat: 7AM-7PM, Sun: 10AM-3PM'
            }
        ]
        
        for clinic_data in clinics_data:
            clinic, created = VeterinaryClinic.objects.get_or_create(
                name=clinic_data['name'],
                defaults=clinic_data
            )
            if created:
                self.stdout.write(f'Created clinic: {clinic.name}')
        
        # Create forum categories
        categories_data = [
            {
                'name': 'General Discussion',
                'description': 'General pet-related discussions',
                'icon': 'bi-chat-dots'
            },
            {
                'name': 'Health & Wellness',
                'description': 'Pet health questions and advice',
                'icon': 'bi-heart-pulse'
            },
            {
                'name': 'Training Tips',
                'description': 'Pet training and behavior discussions',
                'icon': 'bi-award'
            },
            {
                'name': 'Lost & Found',
                'description': 'Report lost or found pets',
                'icon': 'bi-search'
            }
        ]
        
        for category_data in categories_data:
            category, created = ForumCategory.objects.get_or_create(
                name=category_data['name'],
                defaults=category_data
            )
            if created:
                self.stdout.write(f'Created forum category: {category.name}')
        
        self.stdout.write(
            self.style.SUCCESS('Successfully populated sample data!')
        )