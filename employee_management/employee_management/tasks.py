from celery import shared_task
from datetime import timedelta
from django.utils import timezone
from django.core.mail import send_mail
from employee.models import Employee

@shared_task
def send_notification_to_new_employees():
    two_days_ago = timezone.now() - timedelta(days=2)
    new_employees = Employee.objects.filter(date_joined__gt=two_days_ago)

    for employee in new_employees:
        send_mail(
            'Reminder: Complete Your Registration',
            'Please complete your registration process in the system.',
            'from@example.com',  
            [employee.email],  
            fail_silently=False,
        )
