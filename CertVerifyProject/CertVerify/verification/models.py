from django.db import models
from django.contrib.auth.models import User

class Institution(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.name

class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.company_name

class Student(models.Model):
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    student_id = models.CharField(max_length=50, unique=True)
    image = models.ImageField(upload_to='student_images/', blank=True, null=True)

    def __str__(self):
        return self.name

class Certificate(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    certificate_no = models.CharField(max_length=50, unique=True)
    course_name = models.CharField(max_length=255)
    issue_date = models.DateField()
    certificate_file = models.FileField(upload_to='certificates/')

    def __str__(self):
        return f'{self.student.name} - {self.certificate_no}'

class Transcript(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    transcript_file = models.FileField(upload_to='transcripts/')

    def __str__(self):
        return f'{self.student.name} - Transcript'

class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} on {self.created_at}"

class InstitutionRegistration(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Registration Request from {self.name} on {self.created_at}"
