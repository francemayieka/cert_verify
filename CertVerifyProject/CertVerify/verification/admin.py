# verification/admin.py

from django.contrib import admin
from .models import Institution, Employer, Student, Certificate, Transcript

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'student_id', 'institution')
    fields = ('name', 'student_id', 'institution', 'transcript', 'certificate')

class CertificateAdmin(admin.ModelAdmin):
    list_display = ('student', 'certificate_no', 'course_name', 'issue_date')

class TranscriptAdmin(admin.ModelAdmin):
    list_display = ('student',)

admin.site.register(Institution)
admin.site.register(Employer)
admin.site.register(Student, StudentAdmin)
admin.site.register(Certificate, CertificateAdmin)
admin.site.register(Transcript, TranscriptAdmin)
