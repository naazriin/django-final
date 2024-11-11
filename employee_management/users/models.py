from django.db import models
from django.contrib.auth.models import AbstractUser

    
class CustomUser(AbstractUser):
    bio = models.TextField( blank=True, null=True)



class BlackListedIPAddresses(models.Model):
    ip_address = models.GenericIPAddressField()

    def __str__(self):
        return self.ip_address

    class Meta:
        verbose_name_plural = 'Black Listed IP Addresses'
        verbose_name = 'Black Listed IP Address'