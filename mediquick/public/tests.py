from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse
from django.template.loader import render_to_string

# Create your tests here.

class TestBasicViews(TestCase):
    c = Client()

    def test_index(self):
        response = self.c.get(reverse('index'))
        expected_html = render_to_string('public/home.html')
        assert "MediQuick" in expected_html
        assert "public/home.html" in [t.name for t in response.templates]

    def test_forbidden_405(self):
        response = self.c.get(reverse('405'))
        expected_html = render_to_string('public/errors/405.html')
        assert "Oops" in expected_html
        assert "public/errors/405.html" in [t.name for t in response.templates]