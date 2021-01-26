from celery import shared_task
from datetime import datetime
from django.core.mail import send_mail as django_send_mail


# @shared_task
# def scraping_task():
#     django_send_mail('subject', str(datetime.now()), 'noreply@test.com', ['admin@example.com'])

@shared_task
def scraping_task():
    django_send_mail('subject', str(datetime.now()), 'noreply@test.com', ['admin@example.com'])