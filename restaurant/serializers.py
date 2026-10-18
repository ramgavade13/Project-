from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Menu, Booking


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the built-in Django User model.
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'date_joined']


class MenuSerializer(serializers.ModelSerializer):
    """
    Serializer for the Menu model.
    """
    class Meta:
        model = Menu
        fields = ['id', 'title', 'price', 'inventory']


# Backward compatibility alias
MenuItemSerializer = MenuSerializer


class BookingSerializer(serializers.ModelSerializer):
    """
    Serializer for the Booking model.
    """
    class Meta:
        model = Booking
        fields = ['id', 'name', 'no_of_guests', 'booking_date']


# Backward compatibility alias
BookingTableSerializer = BookingSerializer
