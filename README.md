# Pet Care Ecosystem 🐾

A comprehensive web application for pet care management, community interaction, and pet adoption services. Built with Django and designed to be mobile-friendly for your final year CS project.

## Features

### 🏠 Core Features
- **Pet Profiles**: Manage detailed pet information (name, breed, age, photos)
- **Health Records**: Track vaccinations, medical history, and health checkups
- **Feeding Schedules**: Set up and manage feeding reminders
- **Vet Appointments**: Book and manage veterinary appointments
- **Appointment Reminders**: Get notified about upcoming appointments

### 👥 Community Features
- **Pet Owner Forums**: Connect with other pet owners
- **Discussion Categories**: Organized topics for different pet-related discussions
- **Lost Pet Reports**: Report and search for lost pets
- **Tips & Advice Sharing**: Share and discover pet care tips

### 🏡 Adoption Services
- **Adoption Listings**: Browse pets available for adoption
- **Detailed Pet Profiles**: Comprehensive information about adoptable pets
- **Application System**: Apply to adopt pets through the platform
- **Shelter Integration**: Support for animal shelters and rescue organizations

### 🔍 Additional Features
- **Responsible Breeder Listings**: Find verified pet breeders
- **Mobile-Responsive Design**: Works seamlessly on mobile devices
- **User Authentication**: Secure login and registration system
- **Admin Panel**: Comprehensive admin interface for management

## Technology Stack

- **Backend**: Django 4.2.7 + Django REST Framework
- **Database**: MySQL
- **Frontend**: Django Templates + Bootstrap 5
- **Styling**: Bootstrap + Custom CSS
- **Authentication**: Django's built-in authentication system
- **Image Handling**: Pillow for image processing

## Quick Start

### Prerequisites
- Python 3.8+
- MySQL 5.7+ (or SQLite for development)
- pip (Python package manager)
- Gmail account (for email features)

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd pet-care-ecosystem
   ```

2. **Run the setup script**
   ```bash
   python setup.py
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up MySQL database** (Optional - SQLite is default)
   ```sql
   mysql -u root -p
   CREATE DATABASE petcare_db;
   ```

5. **Configure environment variables**
   - Copy `.env.example` to `.env`
   - Update database credentials in `.env`
   - **Configure email settings** (see EMAIL_SETUP.md for detailed instructions)
     ```
     EMAIL_HOST_USER=your-email@gmail.com
     EMAIL_HOST_PASSWORD=your-gmail-app-password
     DEFAULT_FROM_EMAIL=your-email@gmail.com
     ```

6. **Activate virtual environment**
   ```bash
   # Windows
   venv\Scripts\activate
   
   # Mac/Linux
   source venv/bin/activate
   ```

7. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

8. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

9. **Start development server**
   ```bash
   python manage.py runserver
   ```

10. **Access the application**
    - Main site: http://127.0.0.1:8000/
    - Admin panel: http://127.0.0.1:8000/admin/

### Quick Setup Guide

See `QUICK_SETUP.md` for a condensed setup guide with all the essential steps.

### Email Configuration

The application includes email functionality for:
- Welcome emails for new users
- Appointment confirmations
- Adoption application notifications
- Lost pet alerts

See `EMAIL_SETUP.md` for detailed Gmail configuration instructions.

### Image Upload Features

All image uploads are fully configured:
- Breeder photos
- Pet photos
- Profile pictures
- Lost pet photos
- Forum post images
- Adoption listing photos

If you encounter issues, see `IMAGE_UPLOAD_GUIDE.md` for troubleshooting.

## Project Structure

```
petcare_ecosystem/
├── accounts/           # User authentication and profiles
├── pets/              # Pet management and health records
├── appointments/      # Veterinary appointment booking
├── community/         # Forums and lost pet reports
├── adoption/          # Pet adoption listings
├── breeding/          # Breeder listings and reviews
├── templates/         # HTML templates
├── static/           # CSS, JS, and static files
├── media/            # User uploaded files (images)
│   ├── breeders/     # Breeder photos
│   ├── pets/         # Pet photos
│   ├── profiles/     # User profile pictures
│   ├── lost_pets/    # Lost pet photos
│   ├── forum_posts/  # Forum images
│   └── adoption_photos/ # Adoption listing photos
├── petcare_ecosystem/ # Main project settings
│   ├── settings.py   # Django settings
│   ├── urls.py       # URL configuration
│   └── email_utils.py # Email utility functions
├── requirements.txt   # Python dependencies
├── manage.py         # Django management script
├── README.md         # This file
├── QUICK_SETUP.md    # Quick setup guide
├── EMAIL_SETUP.md    # Email configuration guide
├── IMAGE_UPLOAD_GUIDE.md # Image upload troubleshooting
└── test_setup.py     # Setup verification script
```

## API Endpoints

The application includes REST API endpoints for mobile app integration:

- `/api/pets/` - Pet management
- `/api/appointments/` - Appointment booking
- `/api/community/` - Forum posts and discussions
- `/api/adoption/` - Adoption listings

## Development Features

### User Types
- **Pet Owner**: Regular users who own pets
- **Veterinarian**: Vet professionals (future feature)
- **Shelter**: Animal shelter organizations
- **Breeder**: Responsible pet breeders

### Mobile-First Design
- Responsive Bootstrap layout
- Touch-friendly interface
- Optimized for mobile browsers
- Progressive Web App ready

## Contributing

This is a final year project, but contributions and suggestions are welcome:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## Future Enhancements

- Push notifications for reminders
- Real-time chat for community
- GPS integration for lost pets
- Payment integration for adoption fees
- Mobile app (React Native/Flutter)
- AI-powered pet matching for adoption

## License

This project is created for educational purposes as a final year CS project.

## Support

For questions or issues:
- Check the Django documentation
- Review the code comments
- Create an issue in the repository

---

**Made with ❤️ for pets and their humans**