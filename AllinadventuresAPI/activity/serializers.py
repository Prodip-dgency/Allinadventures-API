from rest_framework import serializers 
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import (Location, Category, Gallery, Activity, Content, Event, VirtualActivity, Review)


class LocationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"
        depth = 2

class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        depth = 2

class GalleryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = "__all__"
        depth = 2
        
class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class ActivityModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = "__all__"
        depth = 2

class ContentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = "__all__"
        depth = 2

class EventModelSerializer(serializers.ModelSerializer):
    class Meta:
        model= Event
        fields= "__all__"
        depth = 2

class VirtualActivityModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = VirtualActivity
        fields = "__all__"
        depth = 2

class ReviewModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
        depth = 2


############################ Below is the custom serializers #####################################
class ActivityCustomSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    type = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField()
    age = serializers.CharField()
    duration = serializers.CharField()
    players = serializers.CharField()
    price = serializers.IntegerField()
    slug = serializers.SlugField()
    bg_img = serializers.ImageField()


class EventCustomSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    description = serializers.CharField()
    slug = serializers.CharField()
    bg_img = serializers.ImageField()


class ReviewCustomSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    review_text = serializers.CharField()
    review_author = serializers.CharField()
    author_location = serializers.CharField()