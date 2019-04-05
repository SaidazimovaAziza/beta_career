from django.conf import settings
from django.db import models
from django.utils import timezone


class Company(models.Model):
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name_of_company = models.CharField(max_length=200)
    address = models.TextField()
    description = models.TextField()
    contacts=models.CharField(max_length=200)

    def __str__(self):
        return self.name_of_company
