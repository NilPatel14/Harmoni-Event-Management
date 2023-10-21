from django.shortcuts import render,redirect
from event_data.models import *
from django.conf import settings
# from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User


def add_event(request):
    data = Workhand_category.objects.all()
    active = "add_event"
    context={
        'active' : active,
        'data' : data
    }

    if request.method == "POST":
        return redirect('register')
    
    return render(request , 'vendor/addevent.html',context)
