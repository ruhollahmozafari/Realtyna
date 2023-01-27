
from django.core.mail import send_mail
from django.conf import settings
from celery import shared_task
from realtyna.settings import EMAIL_HOST_USER, EMAIL_HOST
from icecream import ic

@shared_task
def send_email(subject, plain_message, user_email,*args, **kwargs):
    """methdo to send email to user"""
    ic('in the send email method')
    send_mail(subject, plain_message, 
              from_email = EMAIL_HOST_USER, 
              recipient_list=[user_email],)
    return True



