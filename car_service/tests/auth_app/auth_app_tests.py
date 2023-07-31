from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from apps.auth_app.models import AppUsers
from apps.auth_app.forms import CustomerUserCreation, EmployeeUserCreation, CustomPasswordChange



class SignUpViewTest(TestCase):
    def test_sign_up_view(self):
        url = reverse('singup page')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

class UserCreationFormTest(TestCase):
    def test_customer_user_creation_form(self):
        form_data = {
            'username': 'testuser',
            'password1': 'password123__',
            'password2': 'password123__',
            'first_name': 'John',
            'last_name': 'Doe',
        }
        form = CustomerUserCreation(data=form_data)
        self.assertTrue(form.is_valid())

    def test_employee_user_creation_form(self):
        form_data = {
            'username': 'testuser',
            'password1': 'password123__',
            'password2': 'password123__',
        }
        form = EmployeeUserCreation(data=form_data)
        self.assertTrue(form.is_valid())
        
class AppUsersModelTest(TestCase):
    def test_create_app_user(self):
        user = get_user_model().objects.create(username='testuser')
        self.assertIsInstance(user, AppUsers)
        self.assertEqual(user.username, 'testuser')

class FormsTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='password123__'
        )
        
    def test_custom_password_change_form(self):
        form_data = {
            'old_password': 'password123__',
            'new_password1': 'password123!!',
            'new_password2': 'password123!!',
        }
        form = CustomPasswordChange(user=self.user, data=form_data)
        self.assertTrue(form.is_valid())

