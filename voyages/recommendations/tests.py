from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Destination

class DestinationsViewSetTests(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser(username='adminTest', password='azerty123456', email='admintest@test.com')
        self.client.force_authenticate(user=self.superuser)

        self.destination_data = {
            'name': 'Test Destination Name',
            'description': 'Test Destination Description'
        }

        self.test_destination = Destination.objects.create(**self.destination_data)

    def test_list_destinations(self):
        response = self.client.get('http://127.0.0.1:8000/api/destinations/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    def test_create_destination_authenticated_user(self):
        response = self.client.post('http://127.0.0.1:8000/api/destinations/', self.destination_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Destination.objects.count(), 2)
        self.assertEqual(Destination.objects.last().description, 'Test Destination Description')

    def test_retrieve_destination(self):
        response = self.client.get(f'http://127.0.0.1:8000/api/destinations/{self.test_destination.id}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['description'], 'Test Destination Description')

    def test_partial_update_destination_authenticated_user(self):
        updated_data = {'description': 'Updated Test Destination Description'}
        response = self.client.patch(f'http://127.0.0.1:8000/api/destinations/{self.test_destination.id}/', updated_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.test_destination.refresh_from_db()
        self.assertEqual(self.test_destination.description, 'Updated Test Destination Description')

    def test_destroy_destination_authenticated_user(self):
        response = self.client.delete(f'http://127.0.0.1:8000/api/destinations/{self.test_destination.id}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        with self.assertRaises(Destination.DoesNotExist):
            Destination.objects.get(id=self.test_destination.id)

    def test_destroy_destinations_nonexistent(self):
        response = self.client.delete('http://127.0.0.1:8000/api/destinations/9999/')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
