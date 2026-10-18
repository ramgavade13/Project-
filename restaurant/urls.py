from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'tables', views.BookingViewSet, basename='tables')
router.register(r'bookings', views.BookingViewSet, basename='bookings')
router.register(r'users', views.UserViewSet, basename='users')

urlpatterns = [
    # Static HTML content
    path('', views.index, name='index'),

    # Menu API endpoints
    path('menu/', views.MenuItemsView.as_view(), name='menu-list'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name='menu-detail'),
    path('menu-items/', views.MenuItemsView.as_view(), name='menu-items'),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view(), name='menu-item-detail'),

    # Table Booking endpoints
    path('booking/', include(router.urls)),
    path('booking/tables/', views.BookingViewSet.as_view({'get': 'list', 'post': 'create'}), name='booking-tables'),
    path('booking/tables/<int:pk>', views.BookingViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='booking-table-detail'),
    path('bookings/', views.BookingViewSet.as_view({'get': 'list', 'post': 'create'}), name='bookings-list'),
    path('bookings/<int:pk>', views.BookingViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='booking-detail'),

    # User registration
    path('registration/', views.RegistrationView.as_view(), name='registration'),
]
