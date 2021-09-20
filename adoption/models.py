import random
from django.db import models
from django.utils import timezone


""" Creating classes for fixtures so that Django can use them """


def generate_sku():
    random_int = str(random.randint(1000000000, 9999999999))
    unique_ref = 'aa' + random_int
    return str(unique_ref)


class Adoption(models.Model):
    animal = models.CharField(max_length=254)
    animal_plural = models.CharField(max_length=254)
    desc = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    image_header_url = models.URLField(max_length=1024, null=True, blank=True)
    image_header = models.ImageField(null=True, blank=True)
    date_added = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.animal_plural


class Package(models.Model):
    adoption = models.ForeignKey(Adoption, on_delete=models.CASCADE)
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254)
    desc = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    sku = models.CharField(
        max_length=12,
        editable=False,
        unique=True,
        default=generate_sku,
    )

    def save(self, *args, **kwargs):
        self.sku = generate_sku().lower()
        super(Package, self).save(*args, **kwargs)

    def __str__(self):
        return self.friendly_name
