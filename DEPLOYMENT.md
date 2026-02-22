# 🚀 Deployment Guide - Render

## Pre-Deployment Checklist

- [x] All migrations created and applied
- [x] No Django errors (`python manage.py check`)
- [x] Requirements.txt updated
- [x] .env.example provided
- [x] .gitignore configured
- [x] README.md updated

## Environment Variables for Render

Add these in Render Dashboard → Environment:

```
SECRET_KEY=<generate-new-secret-key>
DEBUG=False
GEMINI_API_KEY=AIzaSyA4HMoaI_iyc4EnyyCI-BVSX-TauMsBlNs
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-gmail-app-password
DEFAULT_FROM_EMAIL=your-email@gmail.com
```

## Render Configuration

### Build Command:
```bash
./build.sh
```

### Start Command:
```bash
gunicorn petcare_ecosystem.wsgi:application
```

### Python Version:
```
3.11.0
```
(Specified in runtime.txt)

## Deployment Steps

1. **Push to GitHub**
```bash
git add .
git commit -m "Production ready deployment"
git push origin main
```

2. **Create Web Service on Render**
- Connect GitHub repository
- Select branch: `main`
- Build command: `./build.sh`
- Start command: `gunicorn petcare_ecosystem.wsgi:application`

3. **Add Environment Variables**
- Go to Environment tab
- Add all variables listed above
- Save changes

4. **Deploy**
- Render will automatically build and deploy
- Monitor logs for any errors
- Migrations run automatically via build.sh

## Post-Deployment

### Verify Deployment:
1. Visit your Render URL
2. Test registration/login
3. Test pet creation (without microchip)
4. Test chatbot functionality
5. Test community post creation

### Create Superuser (via Render Shell):
```bash
python manage.py createsuperuser
```

### Check Logs:
Monitor Render logs for any errors or warnings

## Troubleshooting

### Build Fails:
- Check requirements.txt for incompatible versions
- Verify Python version in runtime.txt
- Check build.sh permissions

### Static Files Not Loading:
- Verify WhiteNoise is in MIDDLEWARE
- Check STATIC_ROOT and STATIC_URL settings
- Run `python manage.py collectstatic`

### Database Errors:
- Render provides PostgreSQL automatically
- Check DATABASE_URL is set
- Verify migrations ran successfully

### Chatbot Not Working:
- Verify GEMINI_API_KEY is set
- Check API key is valid
- Monitor logs for API errors

## Security Notes

- ✅ DEBUG=False in production
- ✅ SECRET_KEY is unique and secure
- ✅ ALLOWED_HOSTS configured
- ✅ CSRF protection enabled
- ✅ SQL injection protection (Django ORM)
- ✅ XSS protection enabled
- ⚠️ Consider adding HTTPS redirect
- ⚠️ Consider adding HSTS headers

## Monitoring

### Check Application Health:
```bash
curl https://your-app.onrender.com/
```

### Monitor Logs:
- Render Dashboard → Logs tab
- Watch for errors or warnings
- Check API response times

## Backup

### Database Backup:
Render provides automatic backups for PostgreSQL

### Media Files:
Consider using cloud storage (AWS S3, Cloudinary) for production

## Updates

### Deploy Updates:
```bash
git add .
git commit -m "Update description"
git push origin main
```
Render auto-deploys on push

### Manual Deploy:
Render Dashboard → Manual Deploy button

---

**Your PetCare Ecosystem is ready for production!** 🎉
