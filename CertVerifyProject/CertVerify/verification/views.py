# verification/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserSignupForm, InstitutionSignupForm, EmployerSignupForm, CertificateUploadForm, TranscriptUploadForm
from .models import Certificate

def home(request):
    return render(request, 'verification/home.html')

def institution_signup(request):
    if request.method == 'POST':
        user_form = UserSignupForm(request.POST)
        institution_form = InstitutionSignupForm(request.POST)
        if user_form.is_valid() and institution_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            institution = institution_form.save(commit=False)
            institution.user = user
            institution.save()
            login(request, user)
            return redirect('institution_dashboard')
    else:
        user_form = UserSignupForm()
        institution_form = InstitutionSignupForm()
    return render(request, 'verification/institution_signup.html', {'user_form': user_form, 'institution_form': institution_form})

def employer_signup(request):
    if request.method == 'POST':
        user_form = UserSignupForm(request.POST)
        employer_form = EmployerSignupForm(request.POST)
        if user_form.is_valid() and employer_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            employer = employer_form.save(commit=False)
            employer.user = user
            employer.save()
            login(request, user)
            return redirect('employer_dashboard')
    else:
        user_form = UserSignupForm()
        employer_form = EmployerSignupForm()
    return render(request, 'verification/employer_signup.html', {'user_form': user_form, 'employer_form': employer_form})

def institution_dashboard(request):
    if request.method == 'POST':
        certificate_form = CertificateUploadForm(request.POST, request.FILES)
        transcript_form = TranscriptUploadForm(request.POST, request.FILES)
        if certificate_form.is_valid() and transcript_form.is_valid():
            certificate_form.save()
            transcript_form.save()
            return redirect('institution_dashboard')
    else:
        certificate_form = CertificateUploadForm()
        transcript_form = TranscriptUploadForm()
    return render(request, 'verification/institution_dashboard.html', {'certificate_form': certificate_form, 'transcript_form': transcript_form})

def employer_dashboard(request):
    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        student_id = request.POST.get('student_id')
        certificate_no = request.POST.get('certificate_no')
        course_name = request.POST.get('course_name')
        certificate = Certificate.objects.filter(student__name=student_name, student__student_id=student_id, certificate_no=certificate_no, course_name=course_name).first()
        return render(request, 'verification/employer_dashboard.html', {'certificate': certificate})
    return render(request, 'verification/employer_dashboard.html')
