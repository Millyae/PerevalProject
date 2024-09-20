from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Users, PerevalAdded, Coords

class PerevalTests(APITestCase):
    def setUp(self):
        self.user = Users.objects.create(email="test@example.com")
        self.coord = Coords.objects.create(latitude=50.0, longitude=60.0, height=1000)

    def test_add_pereval(self):
        url = reverse('submit_data')  # укажи правильное имя
        data = {
            "title": "Test Pereval",
            "coord": {
                "latitude": 50.0,
                "longitude": 60.0,
                "height": 1000
            },
            "beauty_title": "Beautiful Pereval"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_pereval_by_id(self):
        pereval = PerevalAdded.objects.create(title="Test", coord=self.coord)
        url = reverse('get_pereval_by_id', args=[pereval.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_pereval(self):
        pereval = PerevalAdded.objects.create(title="Test", coord=self.coord)
        url = reverse('update_pereval', args=[pereval.id])
        data = {
            "title": "Updated Test Pereval",
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        pereval.refresh_from_db()
        self.assertEqual(pereval.title, "Updated Test Pereval")