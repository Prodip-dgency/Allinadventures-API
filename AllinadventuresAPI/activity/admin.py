from django.contrib import admin

from .models import Activity, Location, Category, Gallery, Content

# Register your models here.

admin.site.register([Activity, Location, Category, Gallery, Content])

class ActivityAdminArea(admin.AdminSite):
    site_header = "Activity Database"

activity_site = ActivityAdminArea(name='ActivityAdmin')

activity_site.register(Activity)
activity_site.register(Gallery)
activity_site.register(Content)