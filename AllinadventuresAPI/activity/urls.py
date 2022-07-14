from django.db import router
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()



urlpatterns = [
    path('viewset/', include(router.urls)),
]
