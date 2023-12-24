from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages
from event_data.models import *
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.core.mail import EmailMessage
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

def index(request):
    active = "home"
    context={
        'active' : active
    }
    return render(request , 'user/index.html',context)

def event(request):
    active = "event"
    events = Event.objects.all()
    Event_subcategory_obj = Event_subcategory.objects.all()
    Event_workhand_obj = Event_workhand.objects.all()
    context={
        'active' : active,
        'events' : events,
        'Event_subcategory' : Event_subcategory_obj,
        'Event_Workhand' : Event_workhand_obj,
    }
    return render(request , 'user/event.html',context)

def search_event(request):
    if request.method == "POST":
        search_keyword = request.POST.get('keyword')
        search = request.POST.get('search')
        events = None
        print(search_keyword)
        if not search_keyword == "":
            events = Event.objects.filter(event_name__icontains=search_keyword)
            
            active = "event"
            Event_subcategory_obj = Event_subcategory.objects.all()
            Event_workhand_obj = Event_workhand.objects.all()
            context={
            'active' : active,
            'events' : events,
            'Event_subcategory' : Event_subcategory_obj,
            'Event_Workhand' : Event_workhand_obj,
            }

            return render(request , 'user/event.html',context)

        if search == "all":
            return redirect('event') 
        else:
            events = Event.objects.filter(event_subcategory_id=search) 

        active = "event"
        Event_subcategory_obj = Event_subcategory.objects.all()
        Event_workhand_obj = Event_workhand.objects.all()

        context={
        'active' : active,
        'events' : events,
        'Event_subcategory' : Event_subcategory_obj,
        'Event_Workhand' : Event_workhand_obj,
        }
        return render(request , 'user/event.html',context)

def event_details(request,slug):
    if request.method == 'POST':
        event_details = Event.objects.get(slug=slug)
        contaxt = {
            'event' : event_details,
        }
        return render(request , 'user/event-details.html',contaxt)

def event_register(request,slug):
    if request.method == "POST":
        selected_category = request.POST.get('selected_category')

        if selected_category is not None:
            Event_detail = Event.objects.get(slug=slug)
            workhand = Workhand.objects.get(User_id=request.user)
            workhand_category =  Workhand_category.objects.get(id=selected_category)
            registration = Event_Registrations(workhand_categoty_id=workhand_category , workhand_id = workhand , event_id = Event_detail , company_id = Event_detail.company_id)
            registration.save()
            return redirect('event')
        else:
            pass

    event_details = Event.objects.get(slug=slug)
    event_workhand = Event_workhand.objects.all()
    workhand = Workhand.objects.get(User_id=request.user)
    contaxt={
        'event':event_details,
        'event_workhand' : event_workhand,
        'workhand' : workhand,
    }
    return render(request , 'user/event-register.html',contaxt)

def event_registered(request):
    if request.method=="POST":
        pass

def about(request):
    active = "about"
    context={
        'active' : active
    }
    return render(request , 'user/about.html',context)

def vendor(request):
    active = "vendor"
    contaxt={
        'active' : active
    }
    return render(request , 'user/vendor.html',contaxt)

@login_required(login_url="/accounts/login/")
def contact(request):
    active="contact"
    contaxt={
        'active' : active
    }
    return render(request , 'user/contact.html',contaxt)

def register(request):
    if request.method == "POST":
        role = request.POST.get('role')

        if role == "workhand":
            username = request.POST.get('username')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')
            email = request.POST.get('email')
            contact_number = request.POST.get('contact_number')
            street_address = request.POST.get('street_address')
            state = request.POST.get('state')
            city = request.POST.get('city')
            workhand_category = request.POST.get('workhand_category')
            profile_image = request.FILES.get('profile_image')
            
            #Object Instances--->
            city_obj = City.objects.get(id=city)
            state_obj = State.objects.get(id=state)
            workhand_category_obj = Workhand_category.objects.get(id=workhand_category)
            # ------------------>

            if password and confirm_password:
                if password != confirm_password:
                    messages.error(request , "Password doen's match")
                    return redirect('register')
                else:
                    #save user model
                    user_info = User.objects.create_user(username = username , first_name = first_name , last_name = last_name ,password = password , email = email)
                    user_info.save()

                    #save workhand model
                    Workhand_info = Workhand(first_name=first_name , last_name=last_name , email=email , contact_number=contact_number , street_address=street_address ,state_id=state_obj , city_id=city_obj , profilePic_path=profile_image , Workhand_category_id=workhand_category_obj , User_id=user_info)
                    Workhand_info.save()

                    #save in Porfile model
                    user_profile = profile_pics(User=user_info , image = profile_image)
                    user_profile.save()

                    #user login and redirect
                    auth_login(request,user_info)

                    #Email code 
                    subject = "Sucessfully logedIn!!"
                    msg = f"<p>Hello {first_name} {last_name} !! <br> You are successfully  loge-in into our Harmoni Event Management Website ... we are very greatfull to you..<br> Thank You!!</p>"
                    from_email = settings.EMAIL_HOST_USER
                    msg = EmailMultiAlternatives(subject , msg , from_email , [email])
                    msg.content_subtype = 'html'
                    msg.send()
                    #--------------------#

                    #redirected on index page
                    return redirect('index')
                    #--------------------#

        elif role == "vendor":
            username = request.POST.get('username')
            company_name = request.POST.get('company_name')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')
            email = request.POST.get('email')
            contact_number = request.POST.get('contact_number')
            street_address = request.POST.get('street_address')
            state = request.POST.get('state')
            city = request.POST.get('city')
            discription = request.POST.get('discription')
            company_logo = request.FILES.get('company_logo')

            #Object Instances--->
            city_obj = City.objects.get(id=city)
            state_obj = State.objects.get(id=state)
            # ------------------>

            if password and confirm_password:
                if password != confirm_password:
                    messages.error(request , "Password doen's match")
                    return redirect('register')
                else:
                    #save user model
                    user_info = User.objects.create_user(username = username , first_name = company_name ,password = password , email = email ,is_staff = True)
                    user_info.save()

                    #save company model
                    Company_info = Company(name=company_name , email=email , contact_number=contact_number , street_address=street_address , city_id = city_obj , state_id=state_obj , companyLogo_path = company_logo, description=discription ,User_id=user_info)
                    Company_info.save()
                    
                    # Save in profile table
                    user_profile = profile_pics(User=user_info , image = company_logo)
                    user_profile.save()

                    #user login and redirect
                    auth_login(request,user_info)

                    #Email code 
                    subject = "Sucessfully logedIn!!"
                    msg = f"<p>Hello {company_name} !! <br> You are successfully  loge-in into our Harmoni Event Management Website ... we are very greatfull to you..<br> Thank You!!</p>"
                    from_email = settings.EMAIL_HOST_USER
                    msg = EmailMultiAlternatives(subject , msg , from_email , [email])
                    msg.content_subtype = 'html'
                    msg.send()
                    #--------------------#

                    #redirected on index page
                    return redirect('index')
                    #--------------------#


        else:
            messages.error(request , "Please select role")


    else:
        States = State.objects.all().order_by('-state_name')
        Workhand_categories = Workhand_category.objects.all().order_by('workhand_category_name')
        context = {
            'States' : States,
            'Workhand_category' : Workhand_categories
        }
        return render(request , 'registration/register.html' , context)

def get_city(request):
    state_id = request.GET['state_id']
    get_state = State.objects.get(id=state_id)
    city = City.objects.filter(state_id=get_state)
    return render(request , 'login/get-city.html',locals())
    


def logIn(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('pass')

        user = authenticate(username = username , password = password)

        if user is not None:
            auth_login(request,user)
            if request.GET.get('next' , None):
                return redirect(request.GET['next'])
            return redirect('index')
        else:
            messages.error(request , "Password doen's match")
            return redirect('login')


    return render(request , 'accounts/login.html')

def logout(request):
    try:
        auth_logout(request)
        return redirect('index')
    except e:
        print(e)


@login_required(login_url="/accounts/login/")
def profile(request):
    try:
        if request.user.is_staff:
            company = Company.objects.get(User_id=request.user)
            States = State.objects.all().order_by('-state_name')
            context={
                'company' : company,
                'States' : States,
            }  
        else:
            workhand = Workhand.objects.get(User_id=request.user)
            States = State.objects.all().order_by('-state_name')
            Workhand_categories = Workhand_category.objects.all().order_by('workhand_category_name')
            context={
                'workhand' : workhand,
                'States' : States,
                'Workhand_category' : Workhand_categories,
            }
        return render(request , 'user/profile.html', context)
    except:
        return redirect('index')

def update_profile(request):
    if request.method == "POST":
        if request.user.is_staff:
            company_name = request.POST.get('company_name')
            email = request.POST.get('email')
            contact_number = request.POST.get('contact_number')
            street_address = request.POST.get('street_address')
            state = request.POST.get('state')
            city = request.POST.get('city')
            discription = request.POST.get('discription')
            company_logo = request.FILES.get('company_logo')
            company = Company.objects.get(User_id=request.user)
            profile_id = profile_pics.objects.get(User=request.user)

            file_path = None


            if company_logo is None:
                Company.objects.filter(id=company.id).update(name=company_name , email=email , contact_number=contact_number , street_address=street_address , city_id = city , state_id=state ,  description=discription)
            else:
                file_path = default_storage.save(f'company_img/{company_logo.name}', ContentFile(company_logo.read()))
                Company.objects.filter(id=company.id).update(name=company_name , email=email , contact_number=contact_number , street_address=street_address , city_id = city , state_id=state , companyLogo_path = file_path, description=discription)
                profile_id.image = company_logo
                profile_id.save()
                
            messages.success(request , "Profile Successfully Updated!!")
            return redirect('profile')

        else:
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            contact_number = request.POST.get('contact_number')
            street_address = request.POST.get('street_address')
            state = request.POST.get('state')
            city = request.POST.get('city')
            workhand_category = request.POST.get('workhand_category')
            profile_image = request.FILES.get('profile_image')
            workhand = Workhand.objects.get(User_id=request.user)
            profile_id = profile_pics.objects.get(User=request.user)

            file_path = None

            if profile_image is None:
                Workhand.objects.filter(id=workhand.id).update(first_name=first_name, last_name=last_name , email=email , contact_number=contact_number , street_address=street_address ,state_id=state , city_id=city , Workhand_category_id=workhand_category)
            else:
                file_path = default_storage.save(f'workhand_img/{profile_image.name}', ContentFile(profile_image.read()))
                Workhand.objects.filter(id=workhand.id).update(first_name=first_name, last_name=last_name , email=email , contact_number=contact_number , street_address=street_address ,state_id=state , city_id=city , Workhand_category_id=workhand_category , profilePic_path=file_path)
                profile_id.image = profile_image
                profile_id.save()
            messages.success(request , "Profile Successfully Updated!!")
            return redirect('profile')

            







def error_404(request):
    return render(request, 'login/404-error.html')
