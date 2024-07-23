# verification/admin.py

from django.contrib import admin
from .models import Student, Certificate

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'student_id')

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('student', 'certificate_no', 'course_name', 'certificate_file')
