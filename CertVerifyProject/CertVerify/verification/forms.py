from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import InstitutionRegistration, Employer, ContactMessage

class UserSignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    user_type = forms.ChoiceField(
        choices=[('institution', 'Institution'), ('employer', 'Employer')],
        widget=forms.RadioSelect
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'maxlength': 150}),
            'email': forms.EmailInput(attrs={'maxlength': 254}),
        }
        help_texts = {
            'username': '',  # Remove help text for the username field
            'email': '',     # Optionally remove help text for the email field
            'password': '',  # Optionally remove help text for the password field
        }

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError("Password must be at least 8 characters long.")
        return password

class InstitutionSignupForm(forms.ModelForm):
    class Meta:
        model = InstitutionRegistration
        fields = ['name', 'address', 'email', 'phone_number']
        widgets = {
            'name': forms.TextInput(attrs={'maxlength': 255}),
            'address': forms.TextInput(attrs={'maxlength': 255}),
            'email': forms.EmailInput(attrs={'maxlength': 254}),
            'phone_number': forms.TextInput(attrs={'maxlength': 10}),
        }
        help_texts = {
            'name': '', 
            'address': '',
            'email': '',
            'phone_number': '',
        }

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number and not phone_number.isdigit():
            raise forms.ValidationError("Phone number must contain only digits.")
        if len(phone_number) != 10:
            raise forms.ValidationError("Phone number must be exactly 10 digits long.")
        return phone_number

class EmployerSignupForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = ['company_name', 'address', 'phone_number', 'email']
        widgets = {
            'company_name': forms.TextInput(attrs={'maxlength': 255}),
            'address': forms.TextInput(attrs={'maxlength': 255}),
            'phone_number': forms.TextInput(attrs={'maxlength': 10}),
            'email': forms.EmailInput(attrs={'maxlength': 254}),
        }
        help_texts = {
            'company_name': '',
            'address': '',
            'phone_number': '',
            'email': '',
        }

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number and not phone_number.isdigit():
            raise forms.ValidationError("Phone number must contain only digits.")
        if len(phone_number) != 10:
            raise forms.ValidationError("Phone number must be exactly 10 digits long.")
        return phone_number

class CertificateSearchForm(forms.Form):
    student_name = forms.CharField(max_length=255)
    student_id = forms.CharField(max_length=50)
    certificate_no = forms.CharField(max_length=50)
    course_name = forms.CharField(max_length=255)

    # Removed the custom validation for student_id

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'maxlength': 255}),
            'email': forms.EmailInput(attrs={'maxlength': 254}),
            'message': forms.Textarea(attrs={'maxlength': 2000}),
        }
        help_texts = {
            'name': '',
            'email': '',
            'message': '',
        }

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=254, widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(label="Password", strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}))
