from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Location, Category, Gallery, Activity, Content
from .serializers import LocationModelSerializer, CategoryModelSerializer, GalleryModelSerializer, ActivityModelSerializer, ContentModelSerializer

# Create your views here.

class LocationModelView(viewsets.ModelViewSet):
    serializer_class = LocationModelSerializer
    queryset = Location.objects.all()

class CategoryModelView(viewsets.ModelViewSet):
    serializer_class = CategoryModelSerializer
    queryset = Category.objects.all()

class GalleryModelView(viewsets.ModelViewSet):
    serializer_class = GalleryModelSerializer
    queryset = Gallery.objects.all()

class ActivityModelView(viewsets.ModelViewSet):
    serializer_class = ActivityModelSerializer
    queryset = Activity.objects.all()

class ContentModelView(viewsets.ModelViewSet):
    serializer_class = ContentModelSerializer
    queryset = Content.objects.all()

class ListLocations(APIView):

    def get(self, request, format=None):
        location_list = []
        for location in Location.objects.all():
            location_list = location.title
        return Response(location_list)