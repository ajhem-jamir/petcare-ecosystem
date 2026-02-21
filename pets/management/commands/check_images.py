from django.core.management.base import BaseCommand
from pets.models import Pet
import os


class Command(BaseCommand):
    help = 'Check pet images and their paths'

    def handle(self, *args, **options):
        pets = Pet.objects.all()
        
        self.stdout.write(f"\nTotal pets: {pets.count()}\n")
        
        for pet in pets:
            self.stdout.write(f"\n{pet.name}:")
            self.stdout.write(f"  - Has photo: {bool(pet.photo)}")
            
            if pet.photo:
                self.stdout.write(f"  - Photo name: {pet.photo.name}")
                self.stdout.write(f"  - Photo URL: {pet.photo.url}")
                
                try:
                    self.stdout.write(f"  - Photo path: {pet.photo.path}")
                    self.stdout.write(f"  - File exists: {os.path.exists(pet.photo.path)}")
                    if os.path.exists(pet.photo.path):
                        size = os.path.getsize(pet.photo.path)
                        self.stdout.write(f"  - File size: {size} bytes")
                except Exception as e:
                    self.stdout.write(f"  - Error: {e}")
        
        self.stdout.write("\n")
