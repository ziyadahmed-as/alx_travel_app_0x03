# listings/tasks.py
from celery import shared_task
from django.core.mail import send_mail
from .models import ListOfhotelsBookings

@shared_task
def send_booking_confirmation_email(booking_id):
    try:
        booking = ListOfhotelsBookings.objects.select_related('hotel').get(id=booking_id)
        subject = f"Booking Confirmation for {booking.hotel.name}"
        message = (
            f"Hi {booking.user},\n\n"
            f"Your booking at {booking.hotel.name} has been confirmed!\n"
            f"Check-in: {booking.check_in_date}\n"
            f"Check-out: {booking.check_out_date}\n"
            f"Guests: {booking.number_of_guests}\n\n"
            "Thank you for booking with ALX Travel.\n"
        )
        send_mail(subject, message, None, [f"{booking.user}@example.com"], fail_silently=False)
    except ListOfhotelsBookings.DoesNotExist:
        pass  # or log error
