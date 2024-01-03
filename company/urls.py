from django.urls import path,include
from company import views
from EventManagement import urls

urlpatterns = [
    path("My-events/",views.my_event,name="myevent"),
    path("add-event/" , views.add_event , name="addevent"),
    path("get-subcat/",views.get_subcat , name = "get_subcat"),
    path("workhands-requests/<slug>",views.workhand_requests,name="workhand_requests"),
    path("request-approve/",views.request_approve,name="request_approve"),
    path("payment/<slug>",views.payment , name="payment"),
    path('payment/success/',views.success,name="success"),

    #------- Users Url's path-------#
    # path('',include("EventManagement.urls")),
]