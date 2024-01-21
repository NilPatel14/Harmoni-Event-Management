from django.shortcuts import render,redirect
from event_data.models import *
from django.conf import settings
from EventManagement.settings import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required , user_passes_test
from django.contrib.auth.models import User
import razorpay
from django.views.decorators.csrf import csrf_protect
from django.db.models import Avg
# from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

@login_required(login_url="/accounts/login/")
@user_passes_test(lambda u: u.is_staff, login_url='/404-error/')
def my_event(request):
    active="myevent"
    company_id = Company.objects.get(User_id=request.user)
    Events = Event.objects.filter(company_id=company_id)
    Event_workhand_obj = Event_workhand.objects.all()
    contaxt={
        'active' : active,
        'events' : Events,
        'Event_Workhand' : Event_workhand_obj,
    }
    return render(request,'vendor/company_event.html',contaxt)


@login_required(login_url="/accounts/login/")
@user_passes_test(lambda u: u.is_staff, login_url='/404-error/')
def add_event(request):
    if request.method == "POST":
        Event_Category_id = request.POST.get('cat')
        Event_Subcategory_id = request.POST.get('subcat')
        event_name = request.POST.get('event_name')
        start_datetime = request.POST.get('start_datetime')
        end_datetime = request.POST.get('end_datetime')
        street_address = request.POST.get('street_address')
        state_id = request.POST.get('state')
        city_id = request.POST.get('city')
        description = request.POST.get('description')

        Workhand_categorie = request.POST.getlist('Workhand_categorie')
        price = request.POST.getlist('price')
        workhand_number = request.POST.getlist('workhand_number')
        total_workhand = sum(map(int ,workhand_number))
        total_price = sum(map(int , price))

        #Object Instances--->
        Event_Category_obj = Event_Category.objects.get(id = Event_Category_id)
        Event_subcategory_obj = Event_subcategory.objects.get(id=Event_Subcategory_id)
        city_obj = City.objects.get(id=city_id)
        state_obj = State.objects.get(id=state_id)
        Company_id = Company.objects.get(User_id = request.user)
        # ------------------>
       
        # Save data in Event Table
        Event_info = Event(event_name=event_name , description = description , start_datetime = start_datetime , end_datetime = end_datetime , total_workhand = total_workhand, total_price = total_price ,street_address = street_address , city_id = city_obj , state_id = state_obj , event_category_id = Event_Category_obj , event_subcategory_id = Event_subcategory_obj , company_id = Company_id)
        Event_info.save()

        # Save data in Event_workhand Table
        if len(Workhand_categorie) == len(workhand_number) == len(price):
            for Workhand_category_id, numbers_of_workhand , workhand_price in zip(Workhand_categorie, workhand_number,price):
                Workhand_category_obj = None
                Workhand_category_obj = Workhand_category.objects.get(id=Workhand_category_id)
                Event_workhand_info = Event_workhand(Workhand_category_id = Workhand_category_obj , number_of_workhand=numbers_of_workhand , price = workhand_price , event_id=Event_info )
                Event_workhand_info.save()

            messages.success(request , "Event Successfully Added!!")
            return redirect('addevent')
        
        messages.error(request , "Something Went Wrong!!")
        return redirect('addevent')

    else:
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



@login_required(login_url="/accounts/login/")
@user_passes_test(lambda u: u.is_staff, login_url='/404-error/')
def workhand_requests(request,slug):
    event = Event.objects.get(slug=slug)
    workhands_Requests = Event_Registrations.objects.filter(event_id=event)
    context = {
        'event' : event,
        'workhands_Requests' : workhands_Requests,
    }
    return render(request,'vendor/request_approve.html',context)



@login_required(login_url="/accounts/login/")
@user_passes_test(lambda u: u.is_staff, login_url='/404-error/')
def request_approve(request):
    workhand_id = request.GET.get('workhand_id')
    event_registration_info = Event_Registrations.objects.get(id=workhand_id)
    event_registration_info.registration_status = True
    event_slug=event_registration_info.event_id.slug #for getting slug
    event_registration_info.save()
    return redirect('workhand_requests',slug=event_slug)



@login_required(login_url="/accounts/login/")
@user_passes_test(lambda u: u.is_staff, login_url='/404-error/')
def payment(request,slug):
    event = Event.objects.get(slug=slug)
    Registered_workhand = Event_Registrations.objects.filter(event_id=event , registration_status=True)
    total_price = 0
    for i in Registered_workhand:
        total_price += i.event_workhand_id.price
    context = {
        'event' : event,
        'workhands' : Registered_workhand,
        'total_price' : total_price,
    }
    return render(request,'vendor/payment.html',context)




@login_required(login_url="/accounts/login/")
@user_passes_test(lambda u: u.is_staff, login_url='/404-error/')
def success(request):
    try:
        event_register_id = request.GET.get('workhand_id')
        rate = request.GET.get('rating')
        event_registration_info = Event_Registrations.objects.get(id=event_register_id)
        event_registration_info.payment_status = True
        event_registration_info.rating = rate
        event_registration_info.save()
        print(event_registration_info.workhand_id)
        event_slug=event_registration_info.event_id.slug #for getting slug

        #--------------- Find Average Rating ------------------#
        workhand = event_registration_info.workhand_id #For getting workhand_id and it is used to change avg_rating in workhand model
        average_rating = Event_Registrations.objects.filter(registration_status=True,workhand_id=workhand).aggregate(avg_rating=Avg('rating'))['avg_rating']
        workhand_info = Workhand.objects.get(id=workhand.id) # Get object of Workhand model
        workhand_info.avg_rating = average_rating
        workhand_info.save()
        return redirect('payment', slug=event_slug)
    except:
        messages.error(request , "Something went wrong!!")
        return redirect('payment',slug=event_slug)

def get_subcat(request):
    cat_id = request.GET['cat_id']
    get_cat = Event_Category.objects.get(id = cat_id)
    subcat = Event_subcategory.objects.filter(Event_Category_id = get_cat)
    return render(request , 'vendor/get-subcat.html',locals())
