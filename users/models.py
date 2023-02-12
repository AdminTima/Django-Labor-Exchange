from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
import uuid


class UserManager(BaseUserManager):

    def create_user(self, email, password, **other_fields):
        email = self.normalize_email(email)
        other_fields.setdefault("is_staff", False)
        other_fields.setdefault("is_superuser", False)
        new_user = self.model(email=email, **other_fields)
        new_user.set_password(password)
        new_user.save()
        return new_user

    def create_superuser(self,  email, password, **other_fields):
        other_fields["is_staff"] = True
        other_fields["is_superuser"] = True
        return self.create_user(email, password, **other_fields)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=255, unique=True)
    last_time_visit = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


