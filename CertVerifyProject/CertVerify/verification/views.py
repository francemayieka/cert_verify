from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserSignupForm, InstitutionSignupForm, EmployerSignupForm, CertificateSearchForm
from .models import Institution, Employer, Student, Certificate, Transcript

def home(request):
    return render(request, 'verification/home.html')

def signup(request):
    if request.method == 'POST':
        user_form = UserSignupForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            user_type = user_form.cleaned_data['user_type']
            if user_type == 'institution':
                institution_form = InstitutionSignupForm(request.POST)
                if institution_form.is_valid():
                    institution = institution_form.save(commit=False)
                    institution.user = user
                    institution.save()
            elif user_type == 'employer':
                employer_form = EmployerSignupForm(request.POST)
                if employer_form.is_valid():
                    employer = employer_form.save(commit=False)
                    employer.user = user
                    employer.save()
            auth_login(request, user)
            return redirect('institution_dashboard' if user_type == 'institution' else 'employer_dashboard')
    else:
        user_form = UserSignupForm()
    return render(request, 'verification/signup.html', {'user_form': user_form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            if hasattr(user, 'institution'):
                return redirect('institution_dashboard')
            elif hasattr(user, 'employer'):
                return redirect('employer_dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'verification/login.html', {'form': form})

def logout_view(request):
    from django.contrib.auth import logout
    logout(request)
    return redirect('home')

def institution_dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    try:
        institution = Institution.objects.get(user=request.user)
    except Institution.DoesNotExist:
        return redirect('home')
    
    students = Student.objects.filter(institution=institution)
    return render(request, 'verification/institution_dashboard.html', {'students': students})

def employer_dashboard(request):
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
                return render(request, 'verification/employer_dashboard.html', context)
            except (Student.DoesNotExist, Certificate.DoesNotExist):
                return render(request, 'verification/employer_dashboard.html', {'form': form, 'error': 'Certificate or student not found.'})
    else:
        form = CertificateSearchForm()
    return render(request, 'verification/employer_dashboard.html', {'form': form})

def download_file(request, file_path):
    from django.conf import settings
    from django.http import FileResponse
    import os

    file_path = os.path.join(settings.MEDIA_ROOT, file_path)
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'))
    return HttpResponse("File not found.", status=404)
