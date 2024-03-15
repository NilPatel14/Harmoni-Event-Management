from django.contrib import admin
from event_data.models import *

# For Event_Registration model--#
class Event_register(admin.ModelAdmin):
    list_display = ["event_id","workhand_id","event_workhand_id","company_id","registration_status","payment_status"]
    list_filter = ["registration_status","payment_status","event_id__company_id","event_id","workhand_id"]
    search_fields = ["event_id__event_name" , "workhand_id__first_name" , "workhand_id__last_name","company_id__name"]
#-----------------------------------#

#-- For Event model--#
class Event_workhands(admin.TabularInline):
    model = Event_workhand

class Event_admin(admin.ModelAdmin):
    inlines = [Event_workhands]
    list_display = ["event_name","company_id"]
    list_filter = ["company_id", "start_datetime"]
    search_fields = ["company_id__name","event_name"]
#-----------------------------------#

# For Workhand model --#
class workhandAdmin(admin.ModelAdmin):
    list_display = ["User_id","first_name","last_name"]
    list_filter = ["Workhand_category_id","state_id"]
    search_fields = ["first_name","last_name","User_id__username"]
#-----------------------------------#

# For city model --#
class cityAdmin(admin.ModelAdmin):
    list_filter=["state_id"]
    search_fields = ["city_name"]
#-----------------------------------#

# For Company model --#
class companyModel(admin.ModelAdmin):
    list_display=["name","User_id"]
    search_fields = ["name"]
#-----------------------------------#

# For Event Subcategory --#
class EventSubcategoryAdmin(admin.ModelAdmin):
    list_filter = ["Event_Category_id"]
    search_fields = ["Event_subcategory_name"]
#-----------------------------------#

# For Event_workhand model --#
class EventWorkhandAdmin(admin.ModelAdmin):
    list_display=["event_id","Workhand_category_id","number_of_workhand","price"]
    list_filter = ["event_id__company_id","Workhand_category_id"]
    search_fields = ["event_id__event_name" , "Workhand_category_id__workhand_category_name"]
#-----------------------------------#

# For Feeback model --#
class FeedbackAdmin(admin.ModelAdmin):
    list_display=["workhand_id","event_id","feedback","feedback_date"]
    list_filter = ["event_id"]
    search_fields = ["event_id__event_name"]
#------------------------------------#

# For Workhand_category model -- #
class Workhand_categoryAdmin(admin.ModelAdmin):
    search_fields = ["workhand_category_name"]
#---------------------------------#

admin.site.register(profile_pics)
admin.site.register(Workhand,workhandAdmin)
admin.site.register(Company,companyModel)
admin.site.register(Event,Event_admin)
admin.site.register(Event_workhand,EventWorkhandAdmin)
admin.site.register(Event_Registrations , Event_register)
admin.site.register(Workhand_category,Workhand_categoryAdmin)
admin.site.register(City,cityAdmin)
admin.site.register(State)
admin.site.register(Event_Category)
admin.site.register(Event_subcategory,EventSubcategoryAdmin)
admin.site.register(Feedback,FeedbackAdmin)
# admin.site.register(Payment)