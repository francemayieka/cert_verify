from django import forms
from django.contrib.auth.models import User
from .models import Institution, Employer

class UserSignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    user_type = forms.ChoiceField(
        choices=[('institution', 'Institution'), ('employer', 'Employer')],
        widget=forms.RadioSelect
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class InstitutionSignupForm(forms.ModelForm):
    class Meta:
        model = Institution
        fields = ['name', 'address']

class EmployerSignupForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = ['company_name', 'address']

class CertificateSearchForm(forms.Form):
    student_name = forms.CharField(max_length=255)
    student_id = forms.CharField(max_length=50)
    certificate_no = forms.CharField(max_length=50)
    course_name = forms.CharField(max_length=255)

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()
