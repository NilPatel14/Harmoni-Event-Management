from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages
from event_data.models import *
from django.contrib.auth.decorators import login_required

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
    '''if request.method == "POST":
        role = request.POST.get("role")
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        confirm_password = request.POST.get('confirm_password')

        if password and confirm_password:
            if password != confirm_password:
                messages.error(request , "Password doen's match")
                return redirect('register')
        
            

        if role == "user":
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            number = request.POST.get('number')
            street_address = request.POST.get('street_address')
            city = request.POST.get('city')
            state = request.POST.get('state')
            special_skill = request.POST.get('special_skill')
            profile_image = request.FILES.get('profile_image')
            
            # Save in default user table 
            user = User.objects.create_user(username = username , first_name = first_name , last_name = last_name ,password = password , email = email)
            user.save()

            # Save in Workhand table 
            service_provider_info = Workhand(first_name = first_name , last_name = last_name , email = email , contact = number  , street_address = street_address , city = city , state = state , special_skill = special_skill ,profile_img = profile_image , User = user)
            service_provider_info.save()

            # Save in profile table
            user_profile = profile(User=user , image = profile_image)
            user_profile.save()

            #user login and redirect
            auth_login(request,user)
            return redirect('index')

        if role == "vendor":
            company_name = request.POST.get('company_name')
            number = request.POST.get('number')
            street_address = request.POST.get('street_address')
            city = request.POST.get('city')
            state = request.POST.get('state')
            discription = request.POST.get('discription')
            company_logo = request.FILES.get('company_logo')

            # Save in default user table 
            user = User.objects.create_user(username = username , password = password , email = email , is_staff = True)
            user.save()

            # Save in Company table 
            Company_info = company(name = company_name , email=email , contact=number , street_address= street_address , city = city , state = state , image = company_logo , User = user)
            Company_info.save()

            # Save in profile table
            user_profile = profile(User=user , image = company_logo)
            user_profile.save()

            #user login and redirect
            auth_login(request,user)
            return redirect('index')'''

    States = State.objects.all().order_by('-state_name')
    context = {
        'State' : States
    }
    return render(request , 'login/register.html' , locals())

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


    return render(request , 'login/login.html')

def logout(request):
    try:
        auth_logout(request)
        return redirect('index')
    except e:
        print(e)

def dash(request):
    return render(request , 'vendor/index.html')

def role(request):
    return render(request , 'user/role.html')