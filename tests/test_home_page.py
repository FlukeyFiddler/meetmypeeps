from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from meetmypeeps.views import home_page


class HomepageTest(TestCase):

    def test_home_page_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
