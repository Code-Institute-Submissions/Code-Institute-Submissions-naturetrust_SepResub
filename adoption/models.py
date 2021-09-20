from django.db import models
from django.utils import timezone


""" Creating classes for fixtures so that Django can use them """


class Adoption(models.Model):
    animal = models.CharField(max_length=254)
    animal_plural = models.CharField(max_length=254)
    desc = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    date_added = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.animal_plural


class Package(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254)
    desc = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.friendly_name
