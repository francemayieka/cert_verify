from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from verification import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('verify_certificate/', views.verify_certificate, name='verify_certificate'),
    path('register_institution/', views.register_institution, name='register_institution'),
    path('about/', views.about, name='about'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('download_certificate/<path:file_path>/', views.download_certificate, name='download_certificate'),
    path('download_transcript/<path:file_path>/', views.download_transcript, name='download_transcript'),
    
    # Authentication URLs
    path('login/', LoginView.as_view(template_name='verification/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('signup/', views.user_signup, name='signup'),
]

# Serve static files in development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
