from django.shortcuts import render,redirect
from event_data.models import *
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required , user_passes_test
from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

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

        #Object Instances--->
        Event_Category_obj = Event_Category.objects.get(id = Event_Category_id)
        Event_subcategory_obj = Event_subcategory.objects.get(id=Event_Subcategory_id)
        city_obj = City.objects.get(id=city_id)
        state_obj = State.objects.get(id=state_id)
        Company_id = Company.objects.get(User_id = request.user)
        # ------------------>
       
        # Save data in Event Table
        Event_info = Event(event_name=event_name , description = description , start_datetime = start_datetime , end_datetime = end_datetime , total_workhand = total_workhand ,street_address = street_address , city_id = city_obj , state_id = state_obj , event_category_id = Event_Category_obj , event_subcategory_id = Event_subcategory_obj , company_id = Company_id)
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


def get_subcat(request):
    cat_id = request.GET['cat_id']
    get_cat = Event_Category.objects.get(id = cat_id)
    subcat = Event_subcategory.objects.filter(Event_Category_id = get_cat)
    return render(request , 'vendor/get-subcat.html',locals())
