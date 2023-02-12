import uuid
from django.conf import settings
from django.db import models

# Create your models here.


class Resume(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    phone_number = models.CharField(max_length=30)
    email = models.EmailField()
    city = models.CharField(max_length=120)
    birth_date = models.DateField()
    gender = models.CharField(max_length=100)
    citizenship = models.CharField(max_length=100)
    position = models.CharField(max_length=120)
    keywords = models.TextField()
    desired_salary = models.CharField(max_length=20, null=True)
    work_experience = models.CharField(max_length=40)
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name
