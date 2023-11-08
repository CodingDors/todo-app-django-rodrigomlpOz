from django.test import TestCase, Client
from django.urls import reverse

class ToDoAppTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.index_url = reverse('index')

    def test_get_index(self):
        # Test GET request to index view
        response = self.client.get(self.index_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/index.html')

    def test_post_new_task(self):
        # Test POST request to index view
        response = self.client.post(self.index_url, {'new_task': 'Do laundry'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('Do laundry', response.context['tasks'])
