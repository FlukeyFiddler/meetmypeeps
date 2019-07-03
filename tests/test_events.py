from django.test import TestCase
from meetmypeeps.models import Event
#from django.contrib.gis.geos import Point


class TestEvents(TestCase):

    def test_can_save_POST_request(self):
        data = {'location': '52.2345504, 5.9870061',
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
        first_event.location = (52.2345504, 5.9870061)
        first_event.date = '20-07-2888'
        first_event.save()

        second_event = Event()
        second_event.title = '2nd title'
        second_event.location = (53.2435644, 4.9548342)
        second_event.date = '20-07-2999'
        second_event.save()

        saved_items = Event.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]

        self.assertEqual(first_saved_item.title, first_event.title)
        self.assertEqual(first_saved_item.location, first_event.location)
        self.assertEqual(first_saved_item.date, first_event.date)

        self.assertEqual(second_saved_item.title, second_event.title)
        self.assertEqual(second_saved_item.location, second_event.location)
        self.assertEqual(second_saved_item.date, second_event.date)
