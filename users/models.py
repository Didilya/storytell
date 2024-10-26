from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from model_utils.models import TimeStampedModel
from sorl.thumbnail import ImageField
from users.managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin, TimeStampedModel):
    first_name = models.CharField("first name", max_length=100, blank=True)
    last_name = models.CharField("last name", max_length=100, blank=True)
    email = models.EmailField("email address", db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    thumbnail = ImageField(
        upload_to="users_thumbnails/",
        verbose_name="photo",
        null=True,
        blank=True,
    )

    USERNAME_FIELD = "email"

    objects = CustomUserManager

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    @property
    def is_staff(self):
        return self.is_admin
