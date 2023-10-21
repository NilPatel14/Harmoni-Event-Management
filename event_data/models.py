from django.db import models
from django.contrib.auth.models import User
from indian_cities.dj_city import cities
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from datetime import datetime

class profile(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to = 'profile_img/')

    def __str__(self):
        return f'{self.User.username} profile'

class Workhand_category(models.Model):
    workhand_category = models.CharField(max_length=20)

    def __str__(self):
        return self.workhand_category    

class Workhand(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    contact = models.CharField(max_length=10)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=65)
    state = models.CharField(max_length=65)
    profile_img = models.ImageField(upload_to = 'user_profile_img/' , default = None)
    special_skill = models.CharField(max_length=50 , default=None)
    User = models.ForeignKey('auth.User', null=True , on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name
    

class company(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    contact = models.CharField(max_length=10)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=65)
    state = models.CharField(max_length=65)
    image = models.ImageField(upload_to='vendor_img/' , default=None)
    User = models.ForeignKey('auth.User', blank=True , null=True , on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Events(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_datetime = models.DateTimeField(default = datetime.now)
    end_datetime = models.DateTimeField(default=datetime.now)
    type_of_workhand = models.ManyToManyField(Workhand_category)
    workers_needed = models.IntegerField(default=1) 
    payment = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.ForeignKey('Address',on_delete=models.CASCADE,default=False)
    category = models.ForeignKey('Event_category',on_delete=models.CASCADE,default=False)
    company = models.ForeignKey('company',on_delete=models.CASCADE,default=False)

    def __str__(self):
        return self.name

class feedback(models.Model):
    feedback = models.TextField()
    company = models.ForeignKey('company',on_delete=models.CASCADE,default=False)
    event = models.ForeignKey('Events', on_delete=models.CASCADE)
    workhand = models.ForeignKey('Workhand', on_delete=models.CASCADE)
    

class Address(models.Model):
    street_address = models.CharField(max_length=100)
    city = models.ForeignKey('City',on_delete=models.CASCADE,default=False)
    state = models.ForeignKey('State',on_delete=models.CASCADE,default=False)
    pin_code = models.CharField(max_length=10)

    def __str__(self):
        return f"{street_address},{city},{state} - {pin_code}"
    
class Registrations(models.Model):
    workhand = models.ForeignKey('Workhand', on_delete=models.CASCADE)
    event = models.ForeignKey('Events', on_delete=models.CASCADE)
    company = models.ForeignKey('company',on_delete=models.CASCADE,default=False)
    registration_date = models.DateTimeField(default=datetime.now)
    payment_status = models.BooleanField(default=False)

    def __str__(self):
        return f"Attendee : {self.attendee.name} --> Event : {self.event.name} --> Vendor : {self.event.company.name}"
    
class City(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
            
class State(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
        
class Event_Category(models.Model):
    event_category = models.CharField(max_length=20)

    def __str__(self):
        return self.event_category 

    
