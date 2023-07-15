from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import CustomerProfile
from .forms import ProfileForm
from ..auth_app.models import AppUsers
from ..service_app.models import Cars

User = get_user_model()

class CustomerProfileTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword',
        )
        self.profile = CustomerProfile.objects.create(
            first_name='John',
            last_name='Doe',
            email='john@example.com',
            phone='1234567890',
            user_id=self.user,
        )
        
    def test_profile_creation(self):
        self.assertEqual(str(self.profile), 'John Doe')
        
    def test_profile_form_valid(self):
        form = ProfileForm(data={
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john@example.com',
            'phone': '1234567890',
        })
        self.assertTrue(form.is_valid())
        
    def test_profile_form_invalid(self):
        form = ProfileForm(data={
            'first_name': '',
            'last_name': '',
            'email': 'john@example.com',
            'phone': '1234567890',
        })
        self.assertFalse(form.is_valid())
        
    def test_profile_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')
        self.assertContains(response, 'John Doe')
        
    def test_update_profile_view(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('profile')
        response = self.client.post(url, data={
            'first_name': 'Jane',
            'last_name': 'Doe',
            'email': 'jane@example.com',
            'phone': '9876543210',
        })
        self.assertEqual(response.status_code, 200)
        updated_profile = CustomerProfile.objects.get(user_id=self.user)
        self.assertEqual(updated_profile.first_name, 'Jane')
        self.assertEqual(updated_profile.last_name, 'Doe')
        self.assertEqual(updated_profile.email, 'jane@example.com')
        self.assertEqual(updated_profile.phone, '9876543210')

class CustomUserTest(TestCase):
    def test_user_creation(self):
        user = User.objects.create_user(
            username='testuser',
            password='testpassword',
        )
        self.assertIsInstance(user, AppUsers)
        self.assertEqual(user.username, 'testuser')
        self.assertFalse(user.is_staff)
        self.assertTrue(user.is_active)
        
    def test_user_authentication(self):
        user = User.objects.create_user(
            username='testuser',
            password='testpassword',
        )
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Welcome, testuser')
        
    def test_change_password_view(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('change_password')
        response = self.client.post(url, data={
            'old_password': 'testpassword',
            'new_password1': 'newpassword',
            'new_password2': 'newpassword',
        })
        self.assertEqual(response.status_code, 200)
        updated_user = User.objects.get(username='testuser')
        self.assertTrue(updated_user.check_password('newpassword'))

class CustomerAppTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword',
            is_customer=True,
        )
        
    def test_add_car_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('customer add car page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_car.html')
        # Add more assertions for form submission and data validation
        
    def test_garage_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('garage'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'garage.html')
        self.assertContains(response, 'Test User\'s Garage')
        
    def test_car_repair_process_view(self):
        car = Cars.objects.create(
            brand='Audi',
            model='A4',
            year=2020,
            kilometers=50000,
            VIN='WASDW20201WDA',
            registration_number='CA123456',
            user_id=self.user,
        )
        self.client.login(username='testuser', password='testpassword')
        url = reverse('car process page', args=[car.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'car_repair_process.html')
        self.assertContains(response, 'Repair Process for Car: Audi A4')

    # Add more test cases for other views and functionalities
