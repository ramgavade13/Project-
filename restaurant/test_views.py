from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.models import Menu, Booking
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    """
    Unit tests for Menu API views (/restaurant/menu/ and /api/menu-items/).
    """
    def setUp(self):
        self.client = APIClient()
        self.item1 = Menu.objects.create(title="Greek Salad", price=12.00, inventory=20)
        self.item2 = Menu.objects.create(title="Bruschetta", price=8.50, inventory=15)
        self.item3 = Menu.objects.create(title="Lemon Dessert", price=6.00, inventory=30)

    def test_get_all(self):
        response = self.client.get('/restaurant/menu/')
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_all_api_endpoint(self):
        response = self.client.get('/api/menu-items/')
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_single_item(self):
        response = self.client.get(f'/restaurant/menu/{self.item1.id}')
        serializer = MenuSerializer(self.item1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)


class BookingViewTest(TestCase):
    """
    Unit tests for Table Booking API endpoints.
    """
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testreviewer', password='testpassword123')
        self.booking = Booking.objects.create(
            name="Alice Walker",
            no_of_guests=2,
            booking_date="2026-10-25T18:00:00Z"
        )

    def test_unauthenticated_booking_access_denied(self):
        # Unauthenticated request should be rejected with 401 Unauthorized
        response = self.client.get('/api/bookings/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_get_bookings(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/api/bookings/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_booking_authenticated(self):
        self.client.force_authenticate(user=self.user)
        data = {
            'name': 'Bob Ross',
            'no_of_guests': 4,
            'booking_date': '2026-10-28T19:30:00Z'
        }
        response = self.client.post('/api/bookings/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'Bob Ross')
        self.assertEqual(response.data['no_of_guests'], 4)
