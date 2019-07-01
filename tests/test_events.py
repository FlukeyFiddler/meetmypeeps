from django.test import TestCase
from meetmypeeps.models import Event


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

    def test_save_retrieve_events(self):
        first_event = Event()
        first_event.title = '1st title'
        first_event.lat = '52.2345504'
        first_event.lon = '5.9870061'
        first_event.date = '20-07-2888'
        first_event.save()

        second_event = Event()
        second_event.title = '2nd title'
        second_event.lat = '53.2435644'
        second_event.lon = '4.9548342'
        second_event.date = '20-07-2999'
        second_event.save()

        saved_items = Event.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]

        self.assertEqual(first_saved_item.title, first_event.title)
        self.assertEqual(first_saved_item.lat, first_event.lat)
        self.assertEqual(first_saved_item.lon, first_event.lon)
        self.assertEqual(first_saved_item.date, first_event.date)

        self.assertEqual(second_saved_item.title, second_event.title)
        self.assertEqual(second_saved_item.lat, second_event.lat)
        self.assertEqual(second_saved_item.lon, second_event.lon)
        self.assertEqual(second_saved_item.date, second_event.date)
