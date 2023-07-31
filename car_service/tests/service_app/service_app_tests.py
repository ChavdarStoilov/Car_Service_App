from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from apps.service_app.models import CarBrand, Cars, CarQueue
from apps.service_app.forms import  AddHistoryForm
from django.contrib.auth.models import Group, Permission
from apps.auth_app.forms import EmployeeUserCreation

UserModel = get_user_model()


class EmployeeMechanicUserCreationFormTest(TestCase):
    def test_employee_user_creation_form(self):
        form_data = {
            'username': 'mechanic_test',
            'password1': 'password123__',
            'password2': 'password123__'
        }
        form = EmployeeUserCreation(data=form_data)
        self.assertTrue(form.is_valid())

class EmployeeRecieverUserCreationFormTest(TestCase):
    def test_employee_user_creation_form(self):
        form_data = {
            'username': 'reciever_test',
            'password1': 'password123__',
            'password2': 'password123__'
        }
        form = EmployeeUserCreation(data=form_data)
        self.assertTrue(form.is_valid())
        


class CarsModelTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username='reciever_user_car_test',
            password='password123__',
        )
        
        self.user_customer = get_user_model().objects.create_user(
            username='userCustomer',
            password='password123__',
            is_customer=True
        )
        
        self.group = Group.objects.create(name='Recievers')
        self.permission = Permission.objects.get(codename='add_cars')
        self.group.permissions.add(self.permission)
        self.user.groups.add(self.group)
        self.client.login(username='reciever_user_car_test', password='password123__')

    def test_create_car(self):
        brand = CarBrand.objects.create(
            brand='Toyota',
            image='toyota.png'
        )
        car = Cars.objects.create(
            brand=brand,
            model='Camry',
            year='2021-01-01',
            VIN='1234567890',
            repair=False,
            kilometers='10000',
            registration_number='ABC123',
            have_history=False,
            user_id=self.user_customer
        )
        self.assertIsInstance(car, Cars)
        self.assertEqual(car.brand, brand)
        self.assertEqual(car.model, 'Camry')
        # Add more assertions as needed

class CarQueueModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(username='testuser')
        self.brand = CarBrand.objects.create(
            brand='Toyota',
            image='toyota.png'
        )
        self.car = Cars.objects.create(
            brand=self.brand,
            model='Camry',
            year='2021-01-01',
            VIN='1234567890',
            repair=False,
            kilometers='10000',
            registration_number='ABC123',
            have_history=False,
            user_id=self.user
        )

    def test_create_car_queue(self):
        queue = CarQueue.objects.create(
            car_id=self.car,
            mechanic_id=self.user,
            status='Awaiting To Take'
        )
        self.assertIsInstance(queue, CarQueue)
        self.assertEqual(queue.car_id, self.car)

class AddHistoryFormTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(username='testuser')
        self.brand = CarBrand.objects.create(
            brand='Toyota',
            image='toyota.png'
        )
        self.car = Cars.objects.create(
            brand=self.brand,
            model='Camry',
            year='2021-01-01',
            VIN='1234567890',
            repair=False,
            kilometers='10000',
            registration_number='ABC123',
            have_history=False,
            user_id=self.user
        )

    def test_add_history_form(self):
        form_data = {
            'car_id': self.car.id,
            'history': {
                'Date': '2023-07-15',
                'Kilometers': '15000',
                'Changed parts': {}
            }
        }
        form = AddHistoryForm(data=form_data)
        self.assertTrue(form.is_valid())


class IndexViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username='mechanic_login_test',
            password='password123__'
        )
        self.client.login(username='mechanic_login_test', password='password123__')

    def test_index_view(self):
        url = reverse('service home page')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        # Add more assertions as needed




