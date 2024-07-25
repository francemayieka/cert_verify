# views.py

from django.shortcuts import render, redirect
from django.http import FileResponse, HttpResponse
from django.conf import settings
import os
from django.core.mail import send_mail
from .forms import UserSignupForm, InstitutionSignupForm, CertificateSearchForm, ContactForm
from .models import Institution, Student, Certificate, Transcript

def home(request):
    return render(request, 'verification/home.html')

def verify_certificate(request):
    if request.method == 'POST':
        form = CertificateSearchForm(request.POST)
        if form.is_valid():
            student_name = form.cleaned_data['student_name']
            student_id = form.cleaned_data['student_id']
            certificate_no = form.cleaned_data['certificate_no']
            course_name = form.cleaned_data['course_name']
            try:
                student = Student.objects.get(name=student_name, student_id=student_id)
                certificate = Certificate.objects.get(student=student, certificate_no=certificate_no, course_name=course_name)
                transcript = Transcript.objects.filter(student=student).first()  # Get the transcript if it exists
                
                context = {
                    'form': form,
                    'student': student,  # Include student details
                    'certificate': certificate,
                    'transcript': transcript,
                }
                return render(request, 'verification/verify_certificate.html', context)
            except (Student.DoesNotExist, Certificate.DoesNotExist):
                return render(request, 'verification/verify_certificate.html', {'form': form, 'error': 'Certificate or student not found.'})
    else:
        form = CertificateSearchForm()
    return render(request, 'verification/verify_certificate.html', {'form': form})

def register_institution(request):
    if request.method == 'POST':
        form = InstitutionSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = InstitutionSignupForm()
    return render(request, 'verification/register_institution.html', {'form': form})

def about(request):
    return render(request, 'verification/about_us.html')

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            from_email = form.cleaned_data['email']
            send_mail(subject, message, from_email, ['support@example.com'])
            return render(request, 'verification/contact_us.html', {'form': form, 'success': 'Your message has been sent.'})
    else:
        form = ContactForm()
    return render(request, 'verification/contact_us.html', {'form': form})

def download_file(request, file_path):
    file_path = os.path.join(settings.MEDIA_ROOT, file_path)
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'))
    return HttpResponse("File not found.", status=404)
