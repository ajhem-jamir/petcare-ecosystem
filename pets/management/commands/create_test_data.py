from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from pets.models import Pet
from adoption.models import AdoptionListing, AdoptionPhoto
from breeding.models import BreederListing
from community.models import ForumPost, ForumCategory
from datetime import date, datetime

User = get_user_model()

class Command(BaseCommand):
    help = 'Create test data for demonstration'

    def handle(self, *args, **options):
        self.stdout.write('Creating test data...')
        
        # Create test users
        if not User.objects.filter(username='testowner').exists():
            owner = User.objects.create_user(
                username='testowner',
                email='owner@test.com',
                password='testpass123',
                user_type='owner',
                first_name='John',
                last_name='Doe'
            )
            self.stdout.write(f'Created user: {owner.username}')
        else:
            owner = User.objects.get(username='testowner')
        
        if not User.objects.filter(username='testbreeder').exists():
            breeder = User.objects.create_user(
                username='testbreeder',
                email='breeder@test.com',
                password='testpass123',
                user_type='breeder',
                first_name='Jane',
                last_name='Smith'
            )
            self.stdout.write(f'Created user: {breeder.username}')
        else:
            breeder = User.objects.get(username='testbreeder')
        
        # Create test pets
        if not Pet.objects.filter(name='Buddy').exists():
            pet = Pet.objects.create(
                owner=owner,
                name='Buddy',
                species='dog',
                breed='Golden Retriever',
                gender='male',
                birth_date=date(2022, 3, 15),
                weight=25.5,
                color='Golden',
                microchip_id='123456789012345'
            )
            self.stdout.write(f'Created pet: {pet.name}')
        
        # Create test adoption listing
        if not AdoptionListing.objects.filter(name='Max').exists():
            adoption = AdoptionListing.objects.create(
                lister=owner,
                name='Max',
                species='dog',
                breed='Labrador Mix',
                age_group='young',
                size='large',
                gender='male',
                color='Black and White',
                description='Max is a friendly and energetic dog who loves to play fetch and go on long walks. He is great with kids and other dogs.',
                personality_traits='Friendly, energetic, loyal, good with children',
                is_vaccinated=True,
                is_spayed_neutered=True,
                is_house_trained=True,
                good_with_kids=True,
                good_with_pets=True,
                adoption_fee=2500.00,
                location='Downtown Animal Shelter',
                contact_phone='555-0123',
                contact_email='adopt@shelter.com'
            )
            self.stdout.write(f'Created adoption listing: {adoption.name}')
        
        # Create test breeder listing
        if not BreederListing.objects.filter(business_name='Golden Paws Breeding').exists():
            breeder_listing = BreederListing.objects.create(
                breeder=breeder,
                business_name='Golden Paws Breeding',
                species_specialization='Dogs',
                breeds_available='Golden Retriever, Labrador Retriever, German Shepherd',
                location='Suburban Hills',
                address='123 Breeder Lane, Suburban Hills, ST 12345',
                phone='555-0456',
                email='info@goldenpaws.com',
                website='https://goldenpaws.com',
                description='We are a family-owned breeding operation specializing in healthy, well-socialized puppies. Our dogs are health tested and come with health guarantees.',
                experience_years=15,
                health_testing=True,
                health_guarantee=True,
                certifications='AKC Breeder of Merit, OFA Health Testing',
                verification_status='verified'
            )
            self.stdout.write(f'Created breeder listing: {breeder_listing.business_name}')
        
        # Create test forum posts
        general_category = ForumCategory.objects.get(name='General Discussion')
        
        if not ForumPost.objects.filter(title='Welcome to Pet Care Community!').exists():
            post = ForumPost.objects.create(
                author=owner,
                category=general_category,
                post_type='discussion',
                title='Welcome to Pet Care Community!',
                content='Hello everyone! I\'m excited to be part of this community. Looking forward to sharing experiences and learning from fellow pet owners.'
            )
            self.stdout.write(f'Created forum post: {post.title}')
        
        if not ForumPost.objects.filter(title='Best dog food recommendations?').exists():
            post2 = ForumPost.objects.create(
                author=breeder,
                category=general_category,
                post_type='question',
                title='Best dog food recommendations?',
                content='I\'m looking for recommendations for high-quality dog food for my Golden Retriever. What brands do you all recommend?'
            )
            self.stdout.write(f'Created forum post: {post2.title}')
        
        self.stdout.write(
            self.style.SUCCESS('Successfully created test data!')
        )
        self.stdout.write('Test login credentials:')
        self.stdout.write('Username: testowner, Password: testpass123')
        self.stdout.write('Username: testbreeder, Password: testpass123')