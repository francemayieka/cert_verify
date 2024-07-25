# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('verify_certificate/', views.verify_certificate, name='verify_certificate'),
    path('register_institution/', views.register_institution, name='register_institution'),
    path('about/', views.about, name='about'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('download/<path:file_path>/', views.download_file, name='download_file'),  # Ensure this is included
]
