# verification/forms.py

from django import forms
from django.contrib.auth.models import User
from .models import Institution, Employer, Student, Certificate, Transcript

class UserSignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password_confirm = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        
        if password and password_confirm and password != password_confirm:
            self.add_error('password_confirm', "Passwords do not match")

class InstitutionSignupForm(forms.ModelForm):
    class Meta:
        model = Institution
        fields = ['name', 'address']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Institution Name'}),
            'address': forms.TextInput(attrs={'placeholder': 'Institution Address'}),
        }

class EmployerSignupForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = ['company_name', 'address']
        widgets = {
            'company_name': forms.TextInput(attrs={'placeholder': 'Company Name'}),
            'address': forms.TextInput(attrs={'placeholder': 'Company Address'}),
        }

class CertificateUploadForm(forms.ModelForm):
    student_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Student Name'}))
    class Meta:
        model = Certificate
        fields = ['student', 'certificate_no', 'course_name', 'issue_date', 'certificate_file']
        widgets = {
            'student': forms.Select(attrs={'placeholder': 'Select Student'}),
            'certificate_no': forms.TextInput(attrs={'placeholder': 'Certificate No.'}),
            'course_name': forms.TextInput(attrs={'placeholder': 'Course Name'}),
            'issue_date': forms.DateInput(attrs={'type': 'date'}),
            'certificate_file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['student'].required = False  # Allow typing the student name if not selected

class TranscriptUploadForm(forms.ModelForm):
    class Meta:
        model = Transcript
        fields = ['student', 'transcript_file']
        widgets = {
            'student': forms.Select(attrs={'placeholder': 'Select Student'}),
            'transcript_file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['student'].required = False  # Allow typing the student name if not selected
