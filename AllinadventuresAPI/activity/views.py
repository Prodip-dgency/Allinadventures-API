from django.shortcuts import get_object_or_404, render, HttpResponse

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer

from .models import Location, Category, Gallery, Activity, Content, Event, VirtualActivity, Review
# from .serializers import (LocationModelSerializer, CategoryModelSerializer, 
#                           GalleryModelSerializer, ActivityModelSerializer, 
#                           ContentModelSerializer, EventModelSerializer, 
#                           VirtualActivityModelSerializer, ReviewModelSerializer,
#                           ActivityCustomSerializer, EventCustomSerializer,
#                           ReviewCustomSerializer)

from . import serializers
from .utils import get_absolute_image_path

# Class Based views for all the data tables - Standard

class LocationModelView(viewsets.ModelViewSet):
    serializer_class = serializers.LocationModelSerializer
    queryset = Location.objects.all()

class CategoryModelView(viewsets.ModelViewSet):
    serializer_class = serializers.CategoryModelSerializer
    queryset = Category.objects.all()

class GalleryModelView(viewsets.ModelViewSet):
    serializer_class = serializers.GalleryModelSerializer
    queryset = Gallery.objects.all()

class ActivityModelView(viewsets.ModelViewSet):
    serializer_class = serializers.ActivityModelSerializer
    queryset = Activity.objects.all()

class ContentModelView(viewsets.ModelViewSet):
    serializer_class = serializers.ContentModelSerializer
    queryset = Content.objects.all()

class EventModelView(viewsets.ModelViewSet):
    serializer_class = serializers.EventModelSerializer
    queryset = Event.objects.all()

class VirtualActivityModelView(viewsets.ModelViewSet):
    serializer_class = serializers.VirtualActivityModelSerializer
    queryset = VirtualActivity.objects.all()

class ReviewModelView(viewsets.ModelViewSet):
    serializer_class = serializers.ReviewModelSerializer
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
            serializer = serializers.ActivityCustomSerializer(gameobj, context={'request':request})
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
            serializer = serializers.ActivityCustomSerializer(gameobj, context={'request':request})
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
            serializer = serializers.EventCustomSerializer(eventobj, context={"request":request})
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
            serializer = serializers.ActivityCustomSerializer(gameobj)
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
            serializer = serializers.ReviewCustomSerializer(reviewobj)
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



################################### All location page apis (non standard) ##################################
@api_view()
def allLocationView(request):

    class LocationCustomClass:
        def __init__(self, id, slug, city, state, shortaddress):
            self.id = id
            self.slug = slug
            self.city = city
            self.state = state
            self.shortaddress = shortaddress

    all_locations = Location.objects.all()
    locations = []

    if all_locations:
        for location in all_locations:
            id = location.id
            slug = location.slug
            city = location.city
            state = location.state
            shortaddress = location.title

            locationobj = LocationCustomClass(id, slug, city, state, shortaddress)
            serializer = serializers.LocationCustomSerializer(locationobj)
            locations.append(serializer.data)

    return Response(locations)


################################# Location detail page apis (non standard) ##########################################

@api_view()
def location_details_page_view(request, slug):

    location = get_object_or_404(Location, slug=slug)
    locations = Location.objects.all()
    activities  = Activity.objects.filter(location=location)
    all_events = Event.objects.filter(location=location)
    all_virtual_activities = VirtualActivity.objects.all()
    all_reviews = Review.objects.filter(location=location)
    escaperooms = []
    other_activites = []
    if activities:
        for activity in activities:
            if activity.category:
                if activity.category.title == 'Escape Room':
                    escaperooms.append(activity)
                elif activity.category.title == 'Other Physical Game':
                    other_activites.append(activity)
    
    locationstate = location.state
    locationcity = location.city
    totalLocations = len(locations)
    locationaddress = location.address
    totalUniqueGames = len(activities)
    totalFiveStarReview = "60k+"
    totalPlayerEscaped = "90K+"
    coverimageL = None
    if location.cover_image:
        image_path = location.cover_image.image
        coverimageL = get_absolute_image_path(request, image_path)
    coverimageM = None
    if location.cover_image_mobile:
        image_path = location.cover_image_mobile.image
        coverimageM = get_absolute_image_path(request, image_path)

    pagedata = {
        'locationstate': locationstate,
        'locationcity': locationcity,
        'totalLocations': totalLocations,
        'locationaddress': locationaddress,
        'totalUniqueGames': totalUniqueGames,
        'totalFiveStarReview': totalFiveStarReview,
        'totalPlayerEscaped': totalPlayerEscaped,
        'coverimageL': coverimageL,
        'coverimageM': coverimageM
    }

    
    inpersongames = []
    if escaperooms:
        for escaperoom in escaperooms:
            escaperoom_id = escaperoom.id
            if escaperoom.category:
                escaperoom_category = escaperoom.category.title
            else:
                escaperoom_category = None
            escaperoom_title = escaperoom.title
            escaperoom_description = escaperoom.description
            escaperoom_age = escaperoom.required_age
            escaperoom_duration = escaperoom.duration
            escaperoom_maxplayers = escaperoom.maximum_participant
            escaperoom_minplayers = escaperoom.minimum_participant
            escaperoom_price = escaperoom.price
            escaperoom_slug = escaperoom.slug
            if escaperoom.cover_image:
                image_path = escaperoom.cover_image.image
                escaperoom_bgimg = get_absolute_image_path(request, image_path)
            else:
                escaperoom_bgimg = None

            escaperoom_details = {
                'id': escaperoom_id,
                'category': escaperoom_category,
                'title': escaperoom_title,
                'description': escaperoom_description,
                'age': escaperoom_age,
                'duration': escaperoom_duration,
                'maxplayers': escaperoom_maxplayers,
                'minplayers': escaperoom_minplayers,
                'price': escaperoom_price,
                'slug': escaperoom_slug,
                'bg_img': escaperoom_bgimg
            }
            inpersongames.append(escaperoom_details)

    otherphysicalgames = []
    if other_activites:
        for other_activity in other_activites:
            other_activity_id = other_activity.id
            if other_activity.category:
                other_activity_category = other_activity.category.title
            else:
                other_activity_category = None
            other_activity_title = other_activity.title
            other_activity_description = other_activity.description
            other_activity_age = other_activity.required_age
            other_activity_duration = other_activity.duration
            other_activity_maxplayers = other_activity.maximum_participant
            other_activity_minplayers = other_activity.minimum_participant
            other_activity_price = other_activity.price
            other_activity_slug = other_activity.slug
            if other_activity.cover_image:
                other_activity_bgimg_path = other_activity.cover_image.image
                other_activity_bgimg = get_absolute_image_path(request, other_activity_bgimg_path)
            else:
                other_activity_bgimg = None
            
            other_activity_detials = {
                'id': other_activity_id,
                'category': other_activity_category,
                'title': other_activity_title,
                'description': other_activity_description,
                'age': other_activity_age,
                'duration': other_activity_duration,
                'maxplayers': other_activity_maxplayers,
                'minplayers': other_activity_minplayers,
                'price': other_activity_price,
                'slug': other_activity_slug,
                'bgimg': other_activity_bgimg
            }
            otherphysicalgames.append(other_activity_detials)

    events = []
    if all_events:
        for event in all_events:
            event_id = event.id
            event_title = event.title
            event_description = event.description
            event_slug = event.slug
            if event.cover_image:
                event_bgimg_path = event.cover_image.image
                event_bgimg = get_absolute_image_path(request, event_bgimg_path)
            else:
                event_bgimg = None

            event_details = {
                'id': event_id,
                'title': event_title,
                'description': event_description,
                'slug': event_slug,
                'bgimg': event_bgimg
            }
            events.append(event_details)

    virtualgames = []
    if all_virtual_activities:
        for virtual_activity in all_virtual_activities:
            # 'va' -> virtual activity
            va_id = virtual_activity.id
            if virtual_activity.category:
                va_category = virtual_activity.category.title
            va_title = virtual_activity.title
            va_description = virtual_activity.description
            va_age = virtual_activity.required_age
            va_duration = virtual_activity.duration
            va_maxplayers = virtual_activity.maximum_participant
            va_minplayers = virtual_activity.minimum_participant
            va_price = virtual_activity.price
            va_slug = virtual_activity.slug
            if virtual_activity.cover_image:
                va_bgimg_path = virtual_activity.cover_image.image
                va_bgimg = get_absolute_image_path(request, va_bgimg_path)
            else:
                va_bgimg = None
            
            va_details = {
                'id': va_id,
                'category': va_category,
                'title': va_title,
                'description': va_description,
                'age': va_age,
                'duration': va_duration,
                'maxplayers': va_maxplayers,
                'price': va_minplayers,
                'slug': va_slug,
                'bgimg': va_bgimg,
            }
            virtualgames.append(va_details)


    locationreviews =[]
    if all_reviews:
        for review in all_reviews:
            review_id = review.id
            review_star = review.rating # !----------- Problem ----------------! #
            review_tilte = review.title
            review_text = review.description
            review_author = review.player_name
            if review.location:
                review_author_location = review.location.title
            if review.main_image:
                review_image_path = review.main_image.image
                review_image = get_absolute_image_path(request, review_image_path)
            
            review_details = {
                'id': review_id,
                'star': review_star,
                'tilte': review_tilte,
                'review_text': review_text,
                'author': review_author,
                'author_location': review_author_location,
                'rev_img': review_image 
            }
            locationreviews.append(review_details)

    all_response = {
        'pagedata': pagedata,
        'inpersongames': inpersongames,
        'otherphysicalgames': otherphysicalgames,
        'events': events,
        'virtualgames': virtualgames,
        'locationreviews': locationreviews,
    }

    return Response(all_response)