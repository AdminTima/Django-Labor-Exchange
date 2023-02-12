import uuid
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings


class Employer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company_name = models.CharField(max_length=120)
    company_description = models.TextField()
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="employer"
    )

    def __str__(self):
        return self.company_name
