from django.contrib import admin

from .models import Gallery, Category, Level, Content, Location, Activity, Event, VirtualActivity, Review

# Register your models here.

admin.site.register([Activity, Location, Level, Category, Gallery, Content, Event, VirtualActivity, Review])

class ActivityAdminArea(admin.AdminSite):
    site_header = "Activity Database"
    
activity_site = ActivityAdminArea(name='ActivityAdmin')

activity_site.register(Activity)
activity_site.register(Gallery)
activity_site.register(Content)
activity_site.register(Location)