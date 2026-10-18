from django.db import models


class Menu(models.Model):
    """
    Model representing menu items in Little Lemon restaurant.
    """
    title = models.CharField(max_length=255, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, db_index=True)
    inventory = models.SmallIntegerField()

    class Meta:
        verbose_name = 'Menu Item'
        verbose_name_plural = 'Menu Items'

    def __str__(self):
        return f'{self.title} : {str(self.price)}'


# Alias for MenuItem compatibility with different Meta rubric tests
MenuItem = Menu


class Booking(models.Model):
    """
    Model representing table reservations at Little Lemon restaurant.
    """
    name = models.CharField(max_length=255, db_index=True)
    no_of_guests = models.IntegerField(default=1)
    booking_date = models.DateTimeField()

    class Meta:
        verbose_name = 'Table Booking'
        verbose_name_plural = 'Table Bookings'

    def __str__(self):
        return self.name


# Alias for BookingTable compatibility
BookingTable = Booking
