from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from meetmypeeps.views import home_page


class HomepageTest(TestCase):

    def test_root_resolves_to_homepage(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')

        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>Meet My Peeps', html)
        self.assertTrue(html.endswith('</html>'))

