from dataclasses import fields
from pyexpat import model
from rest_framework.serializers import ModelSerializer

from .models import (Location, Category, Gallery, Activity, Content)


class LocationModelSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"

class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class GalleryModelSerializer(ModelSerializer):
    class Meta:
        model = Gallery
        fields = "__all__"
        

class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class ActivityModelSerializer(ModelSerializer):
    class Meta:
        model = Activity
        fields = "__all__"
        depth = 2

class ContentModelSerializer(ModelSerializer):
    class Meta:
        model = Content
        fields = "__all__"
        depth = 2
