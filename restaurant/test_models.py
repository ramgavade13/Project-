from django.test import TestCase
from django.utils import timezone
from decimal import Decimal
from restaurant.models import Menu, MenuItem, Booking


class MenuItemTest(TestCase):
    """
    Unit tests for the MenuItem / Menu model.
    Tests model instantiation and string representation as required by Meta rubric.
    """
    def test_get_item(self):
        item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream : 80")

    def test_menu_fields(self):
        item = Menu.objects.create(title="Greek Salad", price=Decimal("12.00"), inventory=25)
        self.assertEqual(item.title, "Greek Salad")
        self.assertEqual(item.inventory, 25)
        self.assertEqual(str(item), "Greek Salad : 12.00")


class BookingModelTest(TestCase):
    """
    Unit tests for the Booking model.
    """
    def test_booking_creation(self):
        now = timezone.now()
        booking = Booking.objects.create(
            name="John Doe",
            no_of_guests=4,
            booking_date=now
        )
        self.assertEqual(str(booking), "John Doe")
        self.assertEqual(booking.no_of_guests, 4)
