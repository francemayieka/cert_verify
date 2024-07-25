# verification/urls.py

from django.urls import path
from django.contrib import admin
from .views import home, signup, login_view, logout_view, institution_dashboard, employer_dashboard, download_file

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('institution_dashboard/', institution_dashboard, name='institution_dashboard'),
    path('employer_dashboard/', employer_dashboard, name='employer_dashboard'),
    path('download/<path:file_path>/', download_file, name='download_file'),
    # admin paths
    path('admin/', admin.site.urls),
]

