from django.test import TestCase


class TestEvents(TestCase):

    def test_can_save_POST_request(self):
        data = {'lat': '52.2345504',
                'lon': '5.9870061',
                'title': 'Ma Bday Bash',
                'date': '20-07-2222'
                }
        response = self.client.post('/', data=data)
        self.assertTemplateUsed(response, 'home.html')
        html = response.content.decode()
        for value in data.values():
            self.assertIn(value, html)
