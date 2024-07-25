from django.contrib import admin
from .models import Institution, Employer, Student, Certificate, Transcript

admin.site.register(Institution)
admin.site.register(Employer)
admin.site.register(Student)
admin.site.register(Certificate)
admin.site.register(Transcript)
