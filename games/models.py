from django.db import models
from django.utils import timezone


""" Creating classes for fixtures so that Django can use them """


class Game(models.Model):
    name = models.CharField(max_length=254)
    url_name = models.CharField(max_length=254, null=True, blank=True)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    publisher = models.CharField(max_length=254)
    publisher_friendly_name = models.CharField(max_length=254, null=True, blank=True)
    developer = models.CharField(max_length=254)
    description = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    date_added = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.friendly_name

    def get_friendly_name(self):
        return self.friendly_name


class Edition(models.Model):
    game = models.ForeignKey('Game', on_delete=models.CASCADE)

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    friendly_name_full = models.CharField(max_length=254, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.friendly_name


class Section(models.Model):
    game = models.ForeignKey('Game', on_delete=models.CASCADE)

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    friendly_name_extended = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.friendly_name


class Content(models.Model):
    game = models.ForeignKey('Game', on_delete=models.CASCADE)
    edition = models.ForeignKey('Edition', on_delete=models.CASCADE)
    section = models.ForeignKey('Section', null=True, blank=True, on_delete=models.SET_NULL)

    content = models.CharField(max_length=254)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.content
