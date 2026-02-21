
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.urls import path, include
# Import the function from the pets app
from pets.views import ai_chat 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    
    # The AI Chat Route
    path('ai-chat/', ai_chat, name='ai_chat'),

    path('accounts/', include('accounts.urls')),
    path('pets/', include('pets.urls')),
    path('appointments/', include('appointments.urls')),
    path('community/', include('community.urls')),
    path('adoption/', include('adoption.urls')),
    path('breeding/', include('breeding.urls')),
    path('api/', include('petcare_ecosystem.api_urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
