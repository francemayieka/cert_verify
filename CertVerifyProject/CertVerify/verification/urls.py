# CertVerify/urls.py

from django.contrib import admin
from django.urls import path, include
from verification import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('institution_signup/', views.institution_signup, name='institution_signup'),
    path('employer_signup/', views.employer_signup, name='employer_signup'),
    path('institution_dashboard/', views.institution_dashboard, name='institution_dashboard'),
    path('employer_dashboard/', views.employer_dashboard, name='employer_dashboard'),
    # Other paths
]
