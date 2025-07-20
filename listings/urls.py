from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ListOflocationsViewSet,
    ListOfhotelsViewSet,
    ListOfhotelsImagesViewSet,
    ListOfhotelsReviewsViewSet,
    ListOfhotelsBookingsViewSet,
    initiate_payment,
    verify_payment,
)

router = DefaultRouter()
router.register(r'locations', ListOflocationsViewSet, basename='location')
router.register(r'hotels', ListOfhotelsViewSet, basename='hotel')
router.register(r'hotel-images', ListOfhotelsImagesViewSet, basename='hotelimage')
router.register(r'hotel-reviews', ListOfhotelsReviewsViewSet, basename='hotelreview')
router.register(r'hotel-bookings', ListOfhotelsBookingsViewSet, basename='hotelbooking')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/payment/initiate/', initiate_payment, name='initiate_payment'),
    path('api/payment/verify/', verify_payment, name='verify_payment'),
]
