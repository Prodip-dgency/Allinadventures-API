from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer

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

#testing out APIView class
class ListLocations(APIView):

    def get(self, request, format=None):
        location_list = []
        for location in Location.objects.all():
            location_list = location.title
        return Response(location_list)


#testing out function based view
@api_view()
def homepageview(request):

    #location
    location = Location.objects.all()

    #game
    game = Activity.objects.all()

    #in person game
    inperson_category = get_object_or_404(Category, title='Escape Room') # Needs unique title or create slug
    in_person_games = Activity.objects.all().filter(category = inperson_category)
    in_person_games = ActivityModelSerializer(in_person_games, many=True)
    in_person_games = in_person_games.data
    #above code block needs some safety

    #virtual escape room -----> Coming Soon

    all_response = {
        'location_count': len(location),
        'game_count': len(game),
        'in_person_games': in_person_games
    }

    return Response(all_response)