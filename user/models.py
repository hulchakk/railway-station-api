import os
import uuid

from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import AbstractUser


def create_custom_path(instance, filename):
   _, extension = os.path.splitext(filename)
   return os.path.join(
       "uploads/avatars/",
       f"{slugify(instance.username)}-{uuid.uuid4()}{extension}"
   )


class User(AbstractUser):
    avatar_image = models.ImageField(
        blank=True,
        null=True,
        upload_to=create_custom_path,
    )
