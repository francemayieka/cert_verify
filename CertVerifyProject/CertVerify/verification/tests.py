from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import CertificateSearchForm

class HomePageTests(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

class LoginPageTests(TestCase):
    def test_login_page_template(self):
        response = self.client.get(reverse('login'))
        self.assertTemplateUsed(response, 'verification/login.html')

class CertificateSearchFormTests(TestCase):
    def test_certificate_search_form_initial_state(self):
        response = self.client.get(reverse('verify_certificate'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'name="student_name"')
        self.assertContains(response, 'name="student_id"')
        self.assertContains(response, 'name="certificate_no"')
        self.assertContains(response, 'name="course_name"')

class UserSignupTests(TestCase):
    def test_user_signup(self):
        response = self.client.post(reverse('signup'), {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'password123',
            'password_confirm': 'password123',  # Adjust based on your form
        })
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'testuser')
        self.assertRedirects(response, reverse('verify_certificate'))

class LogoutTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')

    def test_logout_redirect(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('logout'))
        self.assertRedirects(response, reverse('home'))

class AboutPageTests(TestCase):
    def test_about_page_content(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Welcome to CertVerify')
        self.assertContains(response, 'Our mission is to ensure transparency and trust in certificate verification.')
        self.assertContains(response, 'We are constantly innovating to improve our services and meet the needs of our users.')
