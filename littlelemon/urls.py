"""
URL configuration for littlelemon project.
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from restaurant import views

router = DefaultRouter()
router.register(r'tables', views.BookingViewSet, basename='tables')
router.register(r'bookings', views.BookingViewSet, basename='bookings')

urlpatterns = [
    path('admin/', admin.site.urls),

    # Root landing page (serves static HTML content)
    path('', include('restaurant.urls')),

    # Restaurant app URLs (including menu and booking endpoints)
    path('restaurant/', include('restaurant.urls')),
    path('restaurant/booking/', include(router.urls)),

    # Direct API endpoints matching capstone instructions
    path('api/', include('restaurant.urls')),

    # Djoser authentication & registration endpoints
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),

    # DRF Token Authentication endpoint
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
