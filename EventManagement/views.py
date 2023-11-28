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

def index(request):
    active = "home"
    context={
        'active' : active
    }
    return render(request , 'user/index.html',context)

def event(request):
    active = "event"
    context={
        'active' : active
    }
    return render(request , 'user/event.html',context)

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

@login_required(login_url="/login/")
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
                    user_profile = profile(User=user_info , image = profile_image)
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
                    user_profile = profile(User=user_info , image = company_logo)
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

def profile(request):
    return render(request , 'user/profile.html')


def error_404(request):
    return render(request, 'login/404-error.html')
