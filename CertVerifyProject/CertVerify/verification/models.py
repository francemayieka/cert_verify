# verification/models.py

from django.db import models
from django.contrib.auth.models import User

class Institution(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.company_name

class Student(models.Model):
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    student_id = models.CharField(max_length=50, unique=True)

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
