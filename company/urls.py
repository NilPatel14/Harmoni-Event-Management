from django.urls import path,include
from company import views
from EventManagement import urls

urlpatterns = [
    path("add-event/" , views.add_event , name="addevent"),
    path("get-subcat/",views.get_subcat , name = "get_subcat"),

    #------- Users Url's path-------#
    # path('',include("EventManagement.urls")),
]