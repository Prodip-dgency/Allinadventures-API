from django.contrib import admin
from django.db import models

from .models import Gallery, Category, Level, Content, Location, Activity, Event, VirtualActivity, Review
from .widgets import MyWidget

# Register your models here.

# admin.site.register([ Location, Level, Category, Gallery, Content, Event, VirtualActivity, Review])

# @admin.register(Activity)
# class ActivityAdmin(admin.ModelAdmin):
#     list_display = ('title', 'slug', 'category', 'location', 'id', 'titleLength', 'view_section_count')

#     def view_section_count(self, obj):
#         section_count = obj.section.all().count()
#         url = (
#             reverse('admin:activity_content_changelist')
#             + '?'
#             + urlencode({'activity__id': f'{obj.id}'})
#         )
#         return format_html('<a href="{}">Sections ({})</a>', url, section_count)

#     view_section_count.short_description = 'Sections'

###################################################################################################################

# admin.site.register(Activity, ActivityAdmin)

# class ActivityAdminArea(admin.AdminSite):
#     site_header = "Activity Database"
    
# activity_site = ActivityAdminArea(name='ActivityAdmin')

# activity_site.register(Activity)
# activity_site.register(Gallery)
# activity_site.register(Content)
# activity_site.register(Location)

########################################################################################################################

# class ActivityAdminArea(admin.AdminSite):
#     site_header = 'Activity Admin Area'

# activity_site = ActivityAdminArea(name='ActivityAdmin')

# activity_site.register([Location, Activity, VirtualActivity, Gallery, Event, Review])


########################## From Documentation ###########################

class ActivityAdmin(admin.ModelAdmin):
    # fields = ['title', 'description', 'required_age', 'duration', 'minimum_participant', 'maximum_participant', 'price', 'booking_url', 'card_image', 'cover_image', 'cover_image_mobile', 'location', 'level', 'category', 'section']
    fieldsets = [
        ('General', {
            'fields':['title', 'description']
            }
        ),
        ('Automatically generated fields', {
            'fields':['slug']
            }
        ),
        ('Specific information', {
            'fields': [
                'required_age', 
                'duration',
                'minimum_participant',
                'maximum_participant',
            ]}
        ),
        ('Booking related page', {
            'fields': [
                'price',
                'booking_url',
            ]
        })
    ]

    formfield_overrides = {
        models.CharField: {'widget': MyWidget}
    }
    #  = [, , 'required_age', 'duration', 'minimum_participant', 'maximum_participant', 'price', 'booking_url', 'card_image', 'cover_image', 'cover_image_mobile', 'location', 'level', 'category', 'section']

admin.site.register(Activity, ActivityAdmin)