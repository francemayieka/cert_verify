import os
from django.conf import settings
from django.http import FileResponse, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserSignupForm, InstitutionSignupForm, EmployerSignupForm, CertificateSearchForm, ContactForm
from .models import Institution, Employer, Student, Certificate, Transcript

def home(request):
    return render(request, 'verification/home.html')

def user_signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            user = authenticate(username=user.username, password=form.cleaned_data['password'])
            if user:
                login(request, user)
                return redirect('verify_certificate')
    else:
        form = UserSignupForm()
    return render(request, 'verification/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Redirect to the next URL or to 'verify_certificate'
            next_url = request.POST.get('next', 'verify_certificate')
            return redirect(next_url)
    else:
        form = AuthenticationForm()
    # Handle the 'next' parameter in the GET request
    next_url = request.GET.get('next', '')
    return render(request, 'verification/login.html', {'form': form, 'next': next_url})

def user_logout(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
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
            return redirect('home')  # Redirect to home or another page after registration
    else:
        form = InstitutionSignupForm()
    return render(request, 'verification/register_institution.html', {'form': form})

def about(request):
    return render(request, 'verification/about_us.html')

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'verification/contact_us.html', {'form': form, 'success': 'Your message has been sent.'})
    else:
        form = ContactForm()
    return render(request, 'verification/contact_us.html', {'form': form})

def download_certificate(request, file_path):
    file_path = os.path.join(settings.MEDIA_ROOT, file_path)
    if os.path.exists(file_path):
        response = FileResponse(open(file_path, 'rb'))
        response['Content-Disposition'] = 'attachment; filename="certificate.pdf"'
        return response
    return HttpResponse("File not found.", status=404)

def download_transcript(request, file_path):
    file_path = os.path.join(settings.MEDIA_ROOT, file_path)
    if os.path.exists(file_path):
        response = FileResponse(open(file_path, 'rb'))
        response['Content-Disposition'] = 'attachment; filename="transcript.pdf"'
        return response
    return HttpResponse("File not found.", status=404)
