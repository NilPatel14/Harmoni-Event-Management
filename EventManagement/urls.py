"""EventManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from EventManagement import views
from django.conf import settings
from django.conf.urls.static import static 


urlpatterns = [
    path('admin/', admin.site.urls),

    #------------- User Path -----------------#

    #--Header--#
    path('',views.index , name="index"),
    path('event/',views.event , name="event"),
    path('about-us/',views.about , name="about"),
    path('vendor/',views.vendor,name="vendor"),
    path('contact-us/',views.contact , name="contact"),

    #--Login & Logout--#
    path('register/',views.register, name="register"),
    path('get-city/',views.get_city , name = "get_city"),
    path('login/',views.logIn,name="login"),
    path('logout/',views.logout,name="logout"),
    #------------------------------------#

    #-- Company's Path --#
    path('',include("company.urls")),
    #------------------------------------#
] + static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)

