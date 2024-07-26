from django.contrib import admin
from .models import Institution, Employer, Student, Certificate, Transcript, ContactMessage, InstitutionRegistration

class InstitutionAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone_number', 'email')
    list_filter = ('name',)
    search_fields = ('name', 'address', 'phone_number', 'email')

class EmployerAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'email', 'phone_number', 'address')
    list_filter = ('company_name',)
    search_fields = ('company_name', 'email', 'phone_number', 'address')

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'student_id', 'institution')
    list_filter = ('institution',)
    search_fields = ('name', 'student_id')

class CertificateAdmin(admin.ModelAdmin):
    list_display = ('student', 'certificate_no', 'course_name', 'issue_date', 'certificate_file')
    list_filter = ('student', 'course_name')
    search_fields = ('certificate_no', 'course_name')

class TranscriptAdmin(admin.ModelAdmin):
    list_display = ('student', 'transcript_file')
    list_filter = ('student',)
    search_fields = ('student',)

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email')

class InstitutionRegistrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'email', 'phone_number', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'address', 'email', 'phone_number')

# Register your models with custom admin classes
admin.site.register(Institution, InstitutionAdmin)
admin.site.register(Employer, EmployerAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Certificate, CertificateAdmin)
admin.site.register(Transcript, TranscriptAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(InstitutionRegistration, InstitutionRegistrationAdmin)

# Customizing the Django Admin Site header and title
admin.site.site_header = "CertVerify Admin"
admin.site.site_title = "CertVerify Administration"
admin.site.index_title = "Welcome to CertVerify Admin Dashboard"
