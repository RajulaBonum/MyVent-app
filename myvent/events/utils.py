# events/utils.py

from django.core.mail import send_mail
from django.conf import settings

def send_rsvp_confirmation_email(user, event):
    subject = f'RSVP Confirmation for {event.title}'
    message = f'Hi {user.username},\n\nYou have successfully RSVP\'d for the event "{event.title}" happening on {event.date} at {event.location}.\n\nThank you for confirming your attendance!'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user.email]
    send_mail(subject, message, from_email, recipient_list)
