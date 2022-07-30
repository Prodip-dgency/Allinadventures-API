from django.shortcuts import get_object_or_404, render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer

from .models import Location, Category, Gallery, Activity, Content, Event, VirtualActivity, Review
from .serializers import (LocationModelSerializer, CategoryModelSerializer, 
                          GalleryModelSerializer, ActivityModelSerializer, 
                          ContentModelSerializer, EventModelSerializer, 
                          VirtualActivityModelSerializer, ReviewModelSerializer,
                          ActivityCustomSerializer, EventCustomSerializer)


# Class Based views for all the data tables - Standard

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


#function based api for every pages differntly - Not Stadard

@api_view()
def homepageview(request):

    #location
    location = Location.objects.all()
    totalLocations = len(location)

    #game
    game = Activity.objects.all()
    totalUniqueGames = len(game)

    #homeagedata
    homeagedata = {
        'totalLocations': totalLocations,
        'totalUniqueGames': totalUniqueGames,
        'totalFiveStarReview': '98k+',
        'totalPlayerEscaped': '90k+'
    }

    ################## Extra classes ##########################
    class ActivityCustomClass:
        def __init__(self, id, type, title, description, age, duration, players, price, slug, bg_img):
            self.id = id
            self.title = title
            self.type = type
            self.description = description
            self.age = age
            self.duration = duration
            self.players = players
            self.price = price
            self.slug = slug
            self.bg_img = bg_img

    
    class EventCustomClass:
        def __init__(self, id, title, description, slug, bg_img):
            self.id = id
            self.title = title
            self.description = description
            self.slug = slug
            self.bg_img = bg_img


    ############in person game with specified data only#########################

    inpersongames_category = get_object_or_404(Category, title='Escape Room')
    all_inpersongames = Activity.objects.all().filter(category = inpersongames_category)
    inpersongames = []

    if all_inpersongames:
        for game in all_inpersongames:
            id = game.id
            title = game.title
            description = game.description
            age = game.required_age
            duration = game.duration
            players = "{minimum_participant}-{maximum_participant}".format(minimum_participant=game.minimum_participant, maximum_participant=game.maximum_participant)
            price = game.price
            slug = game.slug

            if game.category:
                type = game.category.title
            else:
                type = 'No type defined'
            
            if game.cover_image:
                bg_img = game.cover_image.image
            else:
                bg_img = 'No image uploaded!'

            gameobj = ActivityCustomClass(id, type, title, description, age, duration, players, price, slug, bg_img)
            serializer = ActivityCustomSerializer(gameobj)
            inpersongames.append(serializer.data)
    else:
        data = {'message': 'No game available'}
        inpersongames.append(data)

    ############## otherphysicalgames with specified data only##############################

    otherphysicalgames_category = get_object_or_404(Category, title='Other Physical Game')
    all_otherphysicalgames = Activity.objects.all().filter(category = otherphysicalgames_category)
    otherphysicalgames = []

    if all_otherphysicalgames:
        for game in all_otherphysicalgames:
            id = game.id
            title = game.title
            description = game.description
            age = game.required_age
            duration = game.duration
            players = "{minimum_participant}-{maximum_participant}".format(minimum_participant=game.minimum_participant, maximum_participant=game.maximum_participant)
            price = game.price
            slug = game.slug

            if game.category:
                type = game.category.title
            else:
                type = 'No type defined'
            
            if game.cover_image:
                bg_img = game.cover_image.image
            else:
                bg_img = 'No image is uploaded'

            gameobj = ActivityCustomClass(id, type, title, description, age, duration, players, price, slug, bg_img)
            serializer = ActivityCustomSerializer(gameobj)
            otherphysicalgames.append(serializer.data)
    else:
        data = {'message': 'No game available'}
        otherphysicalgames.append(data)


    ################################ Events with specified data only ################################

    all_events = Event.objects.all()
    events = []

    if all_events:
        for event in all_events:
            id = event.id
            title = event.title
            description = event.description
            slug = event.slug

            if event.cover_image:
                bg_img = event.cover_image.image
            else:
                bg_img = 'No image is uploaded'

            eventobj = EventCustomClass(id, title, description, slug, bg_img)
            serializer = EventCustomSerializer(eventobj)
            events.append(serializer.data)









    # #in person game
    # inperson_category = get_object_or_404(Category, title='Escape Room') # Needs unique title or create slug
    # in_person_games = Activity.objects.all().filter(category = inperson_category)
    # in_person_games = ActivityModelSerializer(in_person_games, many=True)
    # in_person_games = in_person_games.data


    #above code block needs some safety

    #other physical games
    # otherphysicalgames_category = get_object_or_404(Category, title='Other Physical Game')
    # other_physical_games = Activity.objects.all().filter(category=otherphysicalgames_category)
    # other_physical_games = ActivityModelSerializer(other_physical_games, many=True)
    # other_physical_games = other_physical_games.data


    #Events 

    # events = Event.objects.all()
    # events = EventModelSerializer(events, many=True)
    # events = events.data

    #virtual escape room -----> Coming Soon

    virtualgames = VirtualActivity.objects.all()
    virtualgames = VirtualActivityModelSerializer(virtualgames, many=True)
    virtualgames = virtualgames.data

    allreviews = Review.objects.all()
    allreviews = ReviewModelSerializer(allreviews, many=True)
    allreviews = allreviews.data



    all_response = {
        'homeagedata': homeagedata,
        'inpersongames': inpersongames,
        'otherphysicalgames': otherphysicalgames,
        'events': events,
        # 'in_person_games': in_person_games,
        # 'otherphysicalgames': other_physical_games,
        'virtualgames': virtualgames,
        'allreviews': allreviews,
    }

    return Response(all_response)