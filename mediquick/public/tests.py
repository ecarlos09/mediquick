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
        assert "not allowed" in expected_html
        assert "public/errors/405.html" in [t.name for t in response.templates]

    def test_not_found_404(self):
        response = self.c.get(reverse('404'))
        expected_html = render_to_string('public/errors/404.html')
        assert "Oops" in expected_html
        assert "not be found" in expected_html
        assert "public/errors/404.html" in [t.name for t in response.templates]

    def test_server_error_500(self):
        response = self.c.get(reverse('500'))
        expected_html = render_to_string('publicpolicy.html')
        assert "Oops" in expected_html
        assert "not you" in expected_html
        assert "it's us" in expected_html
        assert "public/errors/500.html" in [t.name for t in response.templates]

    def test_policy(self):
        response = self.c.get(reverse('policy'))
        expected_html = render_to_string('public/policy.html')
        assert "Privacy Policy" in expected_html
        assert "mediquick.adm1n@outlook.com" in expected_html
        assert "public/policy.html" in [t.name for t in response.templates]

    def test_about(self):
        response = self.c.get(reverse('about'))
        expected_html = render_to_string('public/about.html')
        assert "Our aim" in expected_html
        assert "public/about.html" in [t.name for t in response.templates]

    def test_support(self):
        response = self.c.get(reverse('support'))
        expected_html = render_to_string('public/support.html')
        assert "mediquick.adm1n@outlook.com" in expected_html
        assert "public/support.html" in [t.name for t in response.templates]
