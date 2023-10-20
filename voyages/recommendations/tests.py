from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import UserProfile

class PostsViewSetTests(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser(username='adminTest', password='azerty123456', email='admintest@test.com')
        self.client.force_authenticate(user=self.superuser)

        self.post_data = {
            'title': 'Test Post Title',
            'body': 'Test Post Content'
        }

        # Changez la ligne suivante pour créer une instance UserProfile
        self.test_post = UserProfile.objects.create(user=self.superuser, preferences="Préférences de test", budget=1000.00)

    def test_list_posts(self):
        response = self.client.get('/userprofiles/')  # URL mise à jour pour les profils d'utilisateur

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    def test_create_post_authenticated_user(self):
        response = self.client.post('/userprofiles/', self.post_data, format='json')  # URL mise à jour pour les profils d'utilisateur

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(UserProfile.objects.count(), 2)
        self.assertEqual(UserProfile.objects.last().preferences, 'Test Post Content')  # Nom du champ mis à jour

    def test_retrieve_post(self):
        response = self.client.get(f'/userprofiles/{self.test_post.id}/')  # URL mise à jour pour les profils d'utilisateur

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['preferences'], 'Préférences de test')  # Nom du champ mis à jour

    def test_partial_update_post_authenticated_user(self):
        updated_data = {'preferences': 'Préférences de test mises à jour'}  # Nom du champ mis à jour
        response = self.client.patch(f'/userprofiles/{self.test_post.id}/', updated_data, format='json')  # URL mise à jour pour les profils d'utilisateur

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.test_post.refresh_from_db()
        self.assertEqual(self.test_post.preferences, 'Préférences de test mises à jour')  # Nom du champ mis à jour

    def test_destroy_post_authenticated_user(self):
        response = self.client.delete(f'/userprofiles/{self.test_post.id}/')  # URL mise à jour pour les profils d'utilisateur

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        with self.assertRaises(UserProfile.DoesNotExist):
            UserProfile.objects.get(id=self.test_post.id)

    def test_destroy_posts_nonexistent(self):
        response = self.client.delete('/userprofiles/9999/')  # URL mise à jour pour les profils d'utilisateur

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
