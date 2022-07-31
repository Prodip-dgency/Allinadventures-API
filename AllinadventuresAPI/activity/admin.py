from itertools import count
from django.contrib import admin
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html

from .models import Gallery, Category, Level, Content, Location, Activity, Event, VirtualActivity, Review

# Register your models here.

admin.site.register([ Location, Level, Category, Gallery, Content, Event, VirtualActivity, Review])

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category', 'location', 'id', 'titleLength', 'view_section_count')

    def view_section_count(self, obj):
        section_count = obj.section.all().count()
        url = (
            reverse('admin:activity_content_changelist')
            + '?'
            + urlencode({'activity__id': f'{obj.id}'})
        )
        return format_html('<a href="{}">Sections ({})</a>', url, section_count)

    view_section_count.short_description = 'Sections'


# admin.site.register(Activity, ActivityAdmin)

# class ActivityAdminArea(admin.AdminSite):
#     site_header = "Activity Database"
    
# activity_site = ActivityAdminArea(name='ActivityAdmin')

# activity_site.register(Activity)
# activity_site.register(Gallery)
# activity_site.register(Content)
# activity_site.register(Location)