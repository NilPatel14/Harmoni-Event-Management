from django.urls import path,include
from company import views
from EventManagement import urls

urlpatterns = [
    path("add-event/" , views.add_event , name="addevent"),
    path("get-subcat/",views.get_subcat , name = "get_subcat"),
    path("event-workhand/",views.event_workhand , name="event_workhand"),
    path('event-workhand/success/',views.success,name="success"),

    #------- Users Url's path-------#
    # path('',include("EventManagement.urls")),
]