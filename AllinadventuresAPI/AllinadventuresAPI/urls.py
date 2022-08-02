from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import settings

from activity import views

# from activity.admin import activity_site

urlpatterns = [
    path('activity/', include('activity.urls')),
    path('admin/', admin.site.urls),
    # path('activityadmin/', activity_site.urls)


    ######################### All the specific  Non-standard apis for each page ##################################
    path('api/homepageview/', views.homepageview, name='homepageview'),
    path('api/all-locations/', views.allLocationView, name='all-locations'),
    path('api/locationhomepage/<slug:slug>', views.location_details_page_view, name='locationdetailspage'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
