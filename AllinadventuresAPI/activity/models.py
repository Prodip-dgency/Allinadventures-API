from tabnanny import verbose
from django.db import models

# Create your models here.

class Location(models.Model):
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=300, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, null=True, blank=True)

    class Meta:
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.title


class Gallery(models.Model):
    title = models.CharField(max_length=20, null=True, blank=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    image = models.ImageField(upload_to='gallery', null=True, blank=True)

    class Meta:
        verbose_name = ("Gallery item")
        verbose_name_plural = ("Gallery")

    def __str__(self):
        return self.title


class Activity(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, null=True, blank=True)
    minimum_participant = models.IntegerField(null=True, blank=True)
    maximum_participant = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    duration = models.CharField(max_length=20, null=True, blank=True)
    cover_image = models.ForeignKey(Gallery, on_delete=models.SET_NULL, null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    external_link = models.CharField(max_length=1000, null=True, blank=True)

    class Meta:
        verbose_name_plural = ("Activities")

    def __str__(self):
        return self.title

   
class Content(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    image = models.ForeignKey(Gallery, on_delete=models.SET_NULL, null=True, blank=True)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
    
