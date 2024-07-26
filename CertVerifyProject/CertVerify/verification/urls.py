from django.contrib import admin
from django.urls import path
from verification import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.user_signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('verify_certificate/', views.verify_certificate, name='verify_certificate'),
    path('register_institution/', views.register_institution, name='register_institution'),
    path('about/', views.about, name='about'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('download_certificate/<path:file_path>/', views.download_certificate, name='download_certificate'),
    path('download_transcript/<path:file_path>/', views.download_transcript, name='download_transcript'),
]
