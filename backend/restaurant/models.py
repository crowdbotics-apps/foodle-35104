from django.conf import settings
from django.db import models


class Restaurant(models.Model):
    "Generated Model"
    name = models.TextField(
        max_length=256,
    )
    street = models.TextField()
    city = models.TextField()
    state = models.TextField()
    zip = models.TextField()
    hot_buttons = models.ManyToManyField(
        "restaurant.HotButton",
        blank=True,
        related_name="restaurant_hot_buttons",
    )


class HotButton(models.Model):
    "Generated Model"
    name = models.TextField()
    icon = models.TextField()


# Create your models here.
