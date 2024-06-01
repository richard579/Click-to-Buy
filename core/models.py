from django.contrib.auth.models import AbstractUser
from django.db import models

# models created here.


class User(AbstractUser):
    email = models.EmailField(unique=True)
