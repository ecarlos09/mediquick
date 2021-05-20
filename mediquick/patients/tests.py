from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

from users.models import CustomUser


# Create your tests here.
# class BaseTestCase(TestCase):
    
#     @classmethod
#     def setUpTestData(cls):
#         cls.poodle_breed = Breed.objects.create(name='Poodle')
#         cls.dog = Dog.objects.create(name='Fido', breed=cls.poodle_breed)
#         cls.user = User.objects.create_user('myusername', 'myemail@crazymail.com', 'mypassword')


# class TestBasicViews(BaseTestCase):
#     c = Client()

#     def test_home(self):
#         response = self.c.get(reverse('adoption-home'))
#         assert "doggos" in response.context
#         assert response.context['doggos'].count() == 1
#         assert "adoption/home.html" in [t.name for t in response.templates]

#     def test_about(self):
#         response = self.c.get(reverse('adoption-about'))
#         assert "adoption/about.html" in [t.name for t in response.templates]

#     def test_create(self):
#         response = self.c.get('dog-create')
#         assert "adoption/404.html" in [t.name for t in response.templates]

#     def test_show(self):
#         response = self.c.get('dog-show')
#         assert "adoption/404.html" in [t.name for t in response.templates]


# class TestLoggedInViews(BaseTestCase):

#     def setUp(self):
#         self.c = Client()
#         self.c.login(username="myusername", password="mypassword")

#     def test_create_page_load(self):
#         response = self.c.get(reverse('dog-create'))
#         assert "dogs/new.html" in [t.name for t in response.templates]

#     def test_create_new_dog(self):
#         response = self.c.post(reverse('dog-create'), {
#             'name': 'new_test_dog',
#             'breed': self.poodle_breed.id
#         })
#         assert Dog.objects.filter(name='new_test_dog').exists()

#     def test_show_page_load(self):
#         response = self.c.get(reverse('dog-show', kwargs={'dog_id': self.dog.id}))
#         assert "dogs/show.html" in [t.name for t in response.templates]
