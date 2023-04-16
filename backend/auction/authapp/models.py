from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True,)

    # following = models.ManyToManyField('self', through='Follow', symmetrical=False, related_name='followers')

    premium_subscribed = models.BooleanField(default=False, blank=False)

    # is_deleted = models.BooleanField(default=False, blank = False)

    # usertype = models.CharField( max_length=20, null=True,
    #     # blank = True,
    #     choices=(
    #         ("client", "Client"),
    #         ("management", "Management"),
    #     ),
    #     default="client",
    # )  # two type of users - 1. client for - i. joining an auction for buying sm, ii. setting up an auction for selling sm and 2. management - for handling auction, changing

    def __str__(self):
        return (f"{self.username} - {self.email}")
