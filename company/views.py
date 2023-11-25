from django.shortcuts import render,redirect
from event_data.models import *
from django.conf import settings
# from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User


def add_event(request):
    if request.method == "POST":
        return redirect('register')

    Event_category = Event_Category.objects.all()
    States = State.objects.all().order_by('-state_name')
    Workhand_categories = Workhand_category.objects.all().order_by('workhand_category_name')
    active = "add_event"
    context={
        'active' : active,
        'States' : States,
        'Workhand_category' : Workhand_categories,
        'Event_category' : Event_category
    }
    return render(request , 'vendor/addevent.html',context)


def get_subcat(request):
    cat_id = request.GET['cat_id']
    get_cat = Event_Category.objects.get(id = cat_id)
    subcat = Event_subcategory.objects.filter(Event_Category_id = get_cat)
    return render(request , 'vendor/get-subcat.html',locals())
