from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.utils import timezone
from decimal import Decimal
from restaurant.models import Menu, Booking


class Command(BaseCommand):
    help = 'Seeds sample menu items, bookings, and test users for Little Lemon'

    def handle(self, *args, **options):
        self.stdout.write('Seeding Little Lemon database...')

        # Create or update superuser
        admin_user, created = User.objects.get_or_create(username='admin', defaults={'email': 'admin@littlelemon.com', 'is_staff': True, 'is_superuser': True})
        if created:
            admin_user.set_password('admin1234')
            admin_user.save()
            self.stdout.write(self.style.SUCCESS('Created superuser: admin / admin1234'))
        Token.objects.get_or_create(user=admin_user)

        # Create or update test customer
        cust_user, created = User.objects.get_or_create(username='customer', defaults={'email': 'customer@littlelemon.com'})
        if created:
            cust_user.set_password('customer1234')
            cust_user.save()
            self.stdout.write(self.style.SUCCESS('Created test user: customer / customer1234'))
        cust_token, _ = Token.objects.get_or_create(user=cust_user)
        self.stdout.write(f'Customer Token: {cust_token.key}')

        # Seed Menu Items
        menu_items = [
            {'title': 'Greek Salad', 'price': Decimal('12.99'), 'inventory': 45},
            {'title': 'Bruschetta', 'price': Decimal('7.99'), 'inventory': 30},
            {'title': 'Lemon Dessert', 'price': Decimal('6.99'), 'inventory': 50},
            {'title': 'Grilled Fish', 'price': Decimal('19.99'), 'inventory': 20},
            {'title': 'Pasta Carbonara', 'price': Decimal('15.50'), 'inventory': 35},
            {'title': 'Mediterranean Platter', 'price': Decimal('18.00'), 'inventory': 25},
        ]

        for item_data in menu_items:
            item, created = Menu.objects.get_or_create(
                title=item_data['title'],
                defaults={'price': item_data['price'], 'inventory': item_data['inventory']}
            )
            if created:
                self.stdout.write(f'Added menu item: {item.title}')

        # Seed Bookings
        now = timezone.now()
        bookings = [
            {'name': 'Adrian Smith', 'no_of_guests': 4, 'booking_date': now + timezone.timedelta(days=1, hours=2)},
            {'name': 'Mario Rossi', 'no_of_guests': 2, 'booking_date': now + timezone.timedelta(days=2, hours=3)},
            {'name': 'Sophia Loren', 'no_of_guests': 6, 'booking_date': now + timezone.timedelta(days=3, hours=1)},
        ]

        for b_data in bookings:
            booking, created = Booking.objects.get_or_create(
                name=b_data['name'],
                defaults={'no_of_guests': b_data['no_of_guests'], 'booking_date': b_data['booking_date']}
            )
            if created:
                self.stdout.write(f'Added booking for: {booking.name}')

        self.stdout.write(self.style.SUCCESS('Database seeded successfully!'))
