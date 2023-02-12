import uuid

from django.contrib.auth.models import User
from django.db import models
from django.conf import settings


class Employee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(
                    settings.AUTH_USER_MODEL,
                    on_delete=models.CASCADE,
                    related_name="employee"
                )
    close_profile = models.BooleanField(default=False)
    in_active_search = models.BooleanField(default=True)

    def __str__(self):
        return self.user.email




