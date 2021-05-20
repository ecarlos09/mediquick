from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse
from django.template.loader import render_to_string

class TestBasicViews(TestCase):
    c = Client()

    def register(self):
        response = self.c.get(reverse('register'))
        expected_html = render_to_string('users/register.html')
        assert "Already have account?" in expected_html
        assert "users/register.html" in [t.name for t in response.templates]

    def auth_view(self):
        response = self.c.get(reverse('login'))
        expected_html = render_to_string('users/register.html')
        assert "No account yet?" in expected_html
        assert "users/login.html" in [t.name for t in response.templates]

    def verify_view(self):
        response = self.c.get(reverse('two-factor-code'))
        expected_html = render_to_string('users/verify.html')
        assert "Submit Code!" in expected_html
        assert "users/verify.html" in [t.name for t in response.templates]

    