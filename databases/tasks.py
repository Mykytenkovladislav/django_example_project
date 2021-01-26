# Create your tasks here
from celery import shared_task

from django.core.mail import send_mail as django_send_mail
