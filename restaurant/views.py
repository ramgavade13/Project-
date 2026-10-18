from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, viewsets, status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer, UserSerializer


def index(request):
    """
    Renders the Little Lemon static HTML home page.
    """
    return render(request, 'index.html', {})


class MenuItemsView(generics.ListCreateAPIView):
    """
    Handles GET (list menu items) and POST (create menu item).
    GET is public; POST requires authentication.
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# Backward compatibility aliases
MenuView = MenuItemsView


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles GET (single item), PUT (update), and DELETE (remove).
    GET is public; PUT/DELETE requires authentication.
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookingViewSet(viewsets.ModelViewSet):
    """
    Handles CRUD operations for table reservations.
    Requires user authentication.
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
    """
    API viewset for managing User accounts.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class RegistrationView(APIView):
    """
    Endpoint for new user registration (/api/registration/).
    Accepts POST request with username, password, and optional email.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email', '')

        if not username or not password:
            return Response(
                {'error': 'Both username and password are required.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        if User.objects.filter(username=username).exists():
            return Response(
                {'error': 'Username already exists.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = User.objects.create_user(username=username, password=password, email=email)
        return Response(
            {
                'message': 'User registered successfully.',
                'id': user.id,
                'username': user.username,
                'email': user.email
            },
            status=status.HTTP_201_CREATED
        )
