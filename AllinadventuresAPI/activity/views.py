from multiprocessing import context
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
                          ActivityCustomSerializer, EventCustomSerializer,
                          ReviewCustomSerializer)


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

class EventModelView(viewsets.ModelViewSet):
    serializer_class = EventModelSerializer
    queryset = Event.objects.all()

class VirtualActivityModelView(viewsets.ModelViewSet):
    serializer_class = VirtualActivityModelSerializer
    queryset = VirtualActivity.objects.all()

class ReviewModelView(viewsets.ModelViewSet):
    serializer_class = ReviewModelSerializer
    queryset = Review.objects.all()


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

    
    class ReviewCustomClass:
        def __init__(self, id, title, review_text, review_author, author_location):
            self.id = id
            self.title = title
            self.review_text = review_text
            self.review_author = review_author
            self.author_location = author_location


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
            serializer = ActivityCustomSerializer(gameobj, context={'request':request})
            inpersongames.append(serializer.data)

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
            serializer = ActivityCustomSerializer(gameobj, context={'request':request})
            otherphysicalgames.append(serializer.data)


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
            serializer = EventCustomSerializer(eventobj, context={"request":request})
            events.append(serializer.data)


    
    ############################Virtual Games##########################################
    all_virtualgames = VirtualActivity.objects.all()
    virtualgames = []

    if all_virtualgames:
        for game in all_virtualgames:
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
            virtualgames.append(serializer.data)


    ################################## Reviews ############################################

    all_reviews = Review.objects.all()
    reviews = []

    if all_reviews:
        for review in all_reviews:
            id = review.id
            title = review.title
            review_text = review.description
            review_author = review.player_name

            if review.location:
                author_location = review.location.title
            else:
                author_location = 'No location specified'
            
            reviewobj = ReviewCustomClass(id, title, review_text, review_author, author_location)
            serializer = ReviewCustomSerializer(reviewobj)
            reviews.append(serializer.data)


    all_response = {
        'homeagedata': homeagedata,
        'inpersongames': inpersongames,
        'otherphysicalgames': otherphysicalgames,
        'events': events,
        'virtualgames': virtualgames,
        'allreviews': reviews,
    }

    return Response(all_response)