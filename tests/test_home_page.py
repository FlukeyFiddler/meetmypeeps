from django.test import TestCase


class HomepageTest(TestCase):

    def test_home_page_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
