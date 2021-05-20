# from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse
from django.template.loader import render_to_string

from users.models import CustomUser


# Create your tests here.
# class BaseTestCase(TestCase):
    
#     @classmethod
#     def setUpTestUser(cls):
#         cls.test_user = CustomUser.objects.create(first_name='Test')
#         cls.user = User.objects.create_user('myusername', 'myemail@crazymail.com', 'mypassword')


# class TestBasicViews(BaseTestCase):
#     c = Client()

#     def test_home(self):
#         response = self.c.get(reverse('index'))
#         assert "doggos" in response.context
#         assert response.context['doggos'].count() == 1
#         assert "public/home.html" in [t.name for t in response.templates]

#         def test_home(self):
#         response = self.c.get(reverse('library-home'))
#         expected_html = render_to_string('home.html')
#         assert "Biblioteca" in expected_html
#         assert "home.html" in [t.name for t in response.templates]

#     def test_about(self):
#         response = self.c.get(reverse('adoption-about'))
#         assert "adoption/about.html" in [t.name for t in response.templates]

#     def test_create(self):
#         response = self.c.get('dog-create')
#         assert "adoption/404.html" in [t.name for t in response.templates]

#     def test_show(self):
#         response = self.c.get('dog-show')
#         assert "adoption/404.html" in [t.name for t in response.templates]


# class TestLoggedInPatientViews(BaseTestCase):

#     def setUp(self):
#         self.c = Client()
#         self.c.login(username="myusername", password="mypassword")

    # def test_load_patient_home(self):
    #     response = self.c.get(reverse('patient-home', kwargs={'user_id': }))
    #     assert "patients/patient-home.html" in [t.name for t in response.templates]

#     def test_create_new_dog(self):
#         response = self.c.post(reverse('dog-create'), {
#             'name': 'new_test_dog',
#             'breed': self.poodle_breed.id
#         })
#         assert Dog.objects.filter(name='new_test_dog').exists()

#     def test_show_page_load(self):
#         response = self.c.get(reverse('dog-show', kwargs={'dog_id': self.dog.id}))
#         assert "dogs/show.html" in [t.name for t in response.templates]
