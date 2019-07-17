from django.test import TestCase
from meetmypeeps.models import Event


class HomepageTest(TestCase):

    def test_home_page_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_post_request(self):
        self.client.get('/')
        self.assertEqual(Event.objects.count(), 0)

