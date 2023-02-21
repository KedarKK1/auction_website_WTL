from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True)
    usertype = models.CharField(
        max_length=20,
        null=True,
        # blank=True,
        choices=(
            ("buyer", "Buyer"),
            ("seller", "Seller"),
            ("management", "Management"),
        ),
        default="buyer",
    )  # three type of users

    def __str__(self):
        return self.username
