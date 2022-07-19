from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('location', views.LocationModelView, basename='location')
router.register('category', views.CategoryModelView, basename='category')
router.register('gallery', views.GalleryModelView, basename='gallery')
router.register('activity', views.ActivityModelView, basename='activity')
router.register('content', views.ContentModelView, basename='content')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('homepageview/', views.homepageview, name='homepageview')
]
