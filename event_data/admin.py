from django.contrib import admin
from event_data.models import *

class Event_workhands(admin.TabularInline):
    model = Event_workhand

class Event_admin(admin.ModelAdmin):
    inlines = [Event_workhands]

admin.site.register(profile_pics)
admin.site.register(Workhand)
admin.site.register(Company)
admin.site.register(Event,Event_admin)
admin.site.register(Event_workhand)
admin.site.register(Event_Registrations)
admin.site.register(Workhand_category)
admin.site.register(City)
admin.site.register(State)
admin.site.register(Event_Category)
admin.site.register(Event_subcategory)
admin.site.register(Feedback)
admin.site.register(Payment)