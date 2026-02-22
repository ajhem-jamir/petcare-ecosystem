# 🐾 PetCare Ecosystem

A comprehensive Django-based web application for pet management, veterinary appointments, community forums, adoption services, and AI-powered pet care recommendations.

## ✨ Features

### Core Features
- **Pet Management** - Add, edit, and track your pets with photos
- **Health Records** - Track vaccinations, checkups, and medical history
- **Appointments** - Schedule and manage vet appointments
- **Community Forum** - Connect with other pet owners
- **Lost & Found** - Report and find lost pets
- **Adoption** - Browse and apply for pet adoption
- **Breeder Directory** - Find reputable breeders

### AI-Powered Features
- **Diet Recommendations** - Veterinary-approved nutritional plans
- **AI Care Assistant** - Personalized care recommendations
- **Smart Chatbot** - Get instant answers about pet care

### Recent Improvements (v2.0)
- ✅ Password visibility toggle on login/registration
- ✅ Optional microchip field for pet registration
- ✅ Real-time password validation
- ✅ Improved form usability and error messages
- ✅ AI chatbot with clear conversation feature

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- pip
- Virtual environment (recommended)

### Installation

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd petcare-ecosystem
```

2. **Create virtual environment**
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure environment**
```bash
cp .env.example .env
# Edit .env with your settings
```

5. **Run migrations**
```bash
python manage.py migrate
```

6. **Create superuser**
```bash
python manage.py createsuperuser
```

7. **Run development server**
```bash
python manage.py runserver
```

8. **Access the application**
- Main site: http://127.0.0.1:8000/
- Admin panel: http://127.0.0.1:8000/admin/

## 🔧 Configuration

### Environment Variables (.env)
```env
SECRET_KEY=your-secret-key
DEBUG=True
GEMINI_API_KEY=your-gemini-api-key
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

### Database
Default: SQLite (db.sqlite3)
For production: Configure PostgreSQL in settings.py

## 📦 Tech Stack

- **Backend**: Django 4.2.7
- **Frontend**: Bootstrap 5, Bootstrap Icons
- **Database**: SQLite (dev), PostgreSQL (production)
- **API**: Django REST Framework
- **AI**: Google Gemini API
- **Deployment**: Render-ready with Gunicorn + WhiteNoise

## 🎯 Key URLs

| Feature | URL |
|---------|-----|
| Home | `/` |
| My Pets | `/pets/` |
| Add Pet | `/pets/add/` |
| Diet Recommendations | `/pets/<id>/diet/` |
| AI Recommendations | `/pets/<id>/ai-recommendations/` |
| Appointments | `/appointments/` |
| Community | `/community/` |
| Lost & Found | `/community/lost-pets/` |
| Adoption | `/adoption/` |

## 📱 Features in Detail

### Diet Recommendation System
- Veterinary-approved formulas (RER & MER)
- Species-specific calculations
- Activity level considerations
- Personalized nutritional breakdown

### AI Care Assistant
- 6 recommendation categories (Health, Nutrition, Exercise, Grooming, Training, General)
- Priority-based action items
- Age and species-specific advice

### Smart Image Management
- Auto-crop to square format (optional)
- Image optimization
- Live preview before upload
- Automatic old image cleanup

## 🚢 Deployment (Render)

1. **Push to GitHub**
```bash
git add .
git commit -m "Ready for deployment"
git push origin main
```

2. **Configure Render**
- Build Command: `./build.sh`
- Start Command: `gunicorn petcare_ecosystem.wsgi:application`

3. **Set Environment Variables**
- Add all variables from .env to Render dashboard
- Set `DEBUG=False` for production

4. **Deploy**
- Render will automatically deploy on push
- Migrations run automatically via build.sh

## 📚 Documentation

- `FIXES_SUMMARY.md` - Recent bug fixes and improvements
- `DIET_FEATURE.md` - Diet recommendation system details
- `PROJECT_FEATURES.md` - Complete feature documentation

## 🛠️ Development

### Run Tests
```bash
python manage.py test
```

### Check for Issues
```bash
python manage.py check
```

### Create Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📄 License

This project is for educational purposes.

## 🐛 Troubleshooting

### Chatbot not responding?
- Check GEMINI_API_KEY in .env
- Verify API key is valid and not leaked
- Check browser console for errors

### Images not displaying?
- Verify media files exist in media/pets/
- Check MEDIA_URL and MEDIA_ROOT settings
- Ensure DEBUG=True for local development

### Email not sending?
- Use Gmail App Password (not regular password)
- Enable 2-Step Verification on Gmail
- Check EMAIL_HOST_USER and EMAIL_HOST_PASSWORD

## 📞 Support

For issues or questions, please open an issue on GitHub.

---

**Built with ❤️ for pet lovers everywhere** 🐶🐱🐦🐰
