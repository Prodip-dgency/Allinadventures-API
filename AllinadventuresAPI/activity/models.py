from django.db import models

from django.db.models.signals import pre_save

from .utils import pre_save_signal_reciever



# Create your models here.


##################### No Dependacny models ###################################

class Gallery(models.Model):
    title = models.CharField(max_length=20, null=True, blank=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    image = models.ImageField(upload_to='gallery', null=True, blank=True)

    class Meta:
        verbose_name = ("Gallery item")
        verbose_name_plural = ("Gallery")

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, null=True, blank=True)

    class Meta:
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.title

class Level(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.title

class Content(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    image = models.ForeignKey(Gallery, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.title


##################### End of No Dependacny models ###################################


class Location(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    desciption = models.CharField(max_length=1000, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    address = models.CharField(max_length=300, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    gps_data = models.CharField(max_length=500, null=True, blank=True)
    card_image = models.ForeignKey(Gallery, on_delete=models.SET_NULL, related_name='location_card_image',null=True, blank=True)
    cover_image = models.ForeignKey(Gallery, on_delete=models.SET_NULL, related_name='location_cover_image', null=True, blank=True)
    cover_image_mobile = models.ForeignKey(Gallery, on_delete=models.SET_NULL, related_name='location_cover_image_mobile', null=True, blank=True)


    def __str__(self):
        return self.title

pre_save.connect(pre_save_signal_reciever, sender=Location)



class Activity(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    required_age = models.CharField(max_length=100, null=True, blank=True)
    duration = models.CharField(max_length=20, null=True, blank=True)
    minimum_participant = models.IntegerField(null=True, blank=True)
    maximum_participant = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    booking_url = models.CharField(max_length=1000, null=True, blank=True)
    card_image = models.ForeignKey(Gallery, on_delete=models.SET_NULL, related_name='activity_card_image', null=True, blank=True)
    cover_image = models.ForeignKey(Gallery, on_delete=models.SET_NULL, related_name='activity_cover_image', null=True, blank=True)
    cover_image_mobile = models.ForeignKey(Gallery, on_delete=models.SET_NULL, related_name='activity_cover_image_mobile', null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)
    level = models.ForeignKey(Level, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    section = models.ManyToManyField(Content, blank=True)

    class Meta:
        verbose_name_plural = ("Activities")
        ordering = ('location', 'category')

    
    def titleLength(obj):
        return len(obj.title)

    def __str__(self):
        return self.title

pre_save.connect(pre_save_signal_reciever, sender=Activity)

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    required_age = models.CharField(max_length=100, null=True, blank=True)
    duration = models.CharField(max_length=10, null=True, blank=True)
    minimum_participant = models.IntegerField(null=True, blank=True)
    maximum_participant = models.IntegerField(null=True, blank=True)
    card_image = models.ForeignKey(Gallery, on_delete=models.SET_NULL, related_name='event_card_image', null=True, blank=True)
    cover_image = models.ForeignKey(Gallery, on_delete=models.SET_NULL, related_name='event_cover_image', null=True, blank=True)
    cover_image_mobile = models.ForeignKey(Gallery, on_delete=models.SET_NULL, related_name='event_cover_image_mobile', null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)
    section = models.ManyToManyField(Content, blank=True)

    def __str__(self):
        return self.title


class VirtualActivity(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    required_age = models.CharField(max_length=100, null=True, blank=True)
    duration = models.CharField(max_length=20, null=True, blank=True)
    minimum_participant = models.IntegerField(null=True, blank=True)
    maximum_participant = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    booking_url = models.CharField(max_length=1000, null=True, blank=True)
    card_image = models.ForeignKey(Gallery, on_delete=models.SET_NULL, related_name='virtualactivity_card_image', null=True, blank=True)
    cover_image = models.ForeignKey(Gallery, on_delete=models.SET_NULL, related_name='virtualactivity_cover_image', null=True, blank=True)
    cover_image_mobile = models.ForeignKey(Gallery, on_delete=models.SET_NULL, related_name='virtualactivity_cover_image_mobile', null=True, blank=True)
    level = models.ForeignKey(Level, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    section = models.ManyToManyField(Content, blank=True)

    class Meta:
        verbose_name_plural = ("Virtual Activities")

    def __str__(self):
        return self.title


class Review(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, null=True, blank=True)
    player_name = models.CharField(max_length=200, blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)
    main_image = models.ForeignKey(Gallery, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title


