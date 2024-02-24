from django.contrib import admin
from event_data.models import *

# For Event_Registration model--#
class Event_register(admin.ModelAdmin):
    list_display = ["event_id","workhand_id","event_workhand_id","company_id","registration_status","payment_status"]
#-----------------------------------#

#-- For Event model--#
class Event_workhands(admin.TabularInline):
    model = Event_workhand

class Event_admin(admin.ModelAdmin):
    list_display = ("event_name","company_id")
    inlines = [Event_workhands]
#-----------------------------------#

# For Workhand model --#
class workhandAdmin(admin.ModelAdmin):
    list_display = ["User_id","first_name","last_name"]
#-----------------------------------#

# For city model --#
class cityAdmin(admin.ModelAdmin):
    list_display = ["city_name","state_id"]
#-----------------------------------#

# For Company model --#
class companyModel(admin.ModelAdmin):
    list_display=["name","User_id"]
#-----------------------------------#

# For Event Subcategory --#
class EventSubcategoryAdmin(admin.ModelAdmin):
    list_display=["Event_subcategory_name","Event_Category_id"]
#-----------------------------------#

# For Event_workhand model --#
class EventWorkhandAdmin(admin.ModelAdmin):
    list_display=["event_id","Workhand_category_id","number_of_workhand","price"]
#-----------------------------------#

# For Feeback model --#
class FeedbackAdmin(admin.ModelAdmin):
    list_display=["workhand_id","event_id","feedback","feedback_date"]
#------------------------------------#

admin.site.register(profile_pics)
admin.site.register(Workhand,workhandAdmin)
admin.site.register(Company,companyModel)
admin.site.register(Event,Event_admin)
admin.site.register(Event_workhand,EventWorkhandAdmin)
admin.site.register(Event_Registrations , Event_register)
admin.site.register(Workhand_category)
admin.site.register(City,cityAdmin)
admin.site.register(State)
admin.site.register(Event_Category)
admin.site.register(Event_subcategory,EventSubcategoryAdmin)
admin.site.register(Feedback,FeedbackAdmin)
# admin.site.register(Payment)