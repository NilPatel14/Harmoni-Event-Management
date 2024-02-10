from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from .utils import generate_slug , generate_slug_comapny , generate_slug_workhand
from ckeditor.fields import RichTextField
from django.core.validators import MaxValueValidator, MinValueValidator

class profile_pics(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to = 'profile_img/')

    def __str__(self):
        return f'{self.User.username} profile'

class Workhand(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    contact_number = models.CharField(max_length=12)
    street_address = models.CharField(max_length=200)
    city_id = models.ForeignKey('City', on_delete=models.CASCADE)
    state_id = models.ForeignKey('State' , on_delete=models.CASCADE)
    profilePic_path = models.ImageField(default = 'default.jpg' , upload_to = 'workhand_img/')
    Workhand_category_id = models.ForeignKey('Workhand_category' , on_delete=models.CASCADE)
    avg_rating = models.IntegerField(default=1, validators=[MaxValueValidator(5),MinValueValidator(1)])
    User_id = models.ForeignKey('auth.User',  on_delete=models.CASCADE)

    slug = models.SlugField(unique = True , null=True , blank=True , max_length=100)

    def save(self , *args , **kwargs):
        self.slug = generate_slug_workhand(self.first_name)
        super(Workhand , self).save(*args , **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Company(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    contact_number = models.CharField(max_length=12)
    street_address = models.CharField(max_length=200)
    city_id = models.ForeignKey('City', on_delete=models.CASCADE)
    state_id = models.ForeignKey('State' , on_delete=models.CASCADE)
    companyLogo_path = models.ImageField(default='default.jpg' , upload_to = 'company_img/')
    description = models.TextField(default=None)
    User_id = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    slug = models.SlugField(unique = True , null=True , blank=True , max_length=100)

    def save(self , *args , **kwargs):
        self.slug = generate_slug_comapny(self.name)
        super(Company , self).save(*args , **kwargs)

    def __str__(self):
        return self.name
    

class Event(models.Model):
    event_name = models.CharField(max_length=255)
    description = RichTextField(null=True)
    start_datetime = models.DateTimeField(default = datetime.now)
    end_datetime = models.DateTimeField(default=datetime.now)
    total_workhand = models.IntegerField(default=11) 
    total_price = models.IntegerField(null=True)
    street_address = models.CharField(max_length=250)
    city_id = models.ForeignKey('City', on_delete=models.CASCADE)
    state_id = models.ForeignKey('State' , on_delete=models.CASCADE)
    event_category_id = models.ForeignKey('Event_category',on_delete=models.CASCADE,default=False)
    event_subcategory_id = models.ForeignKey('Event_subcategory',on_delete=models.CASCADE,null=True)
    company_id = models.ForeignKey('company',on_delete=models.CASCADE,default=False)
    slug = models.SlugField(unique = True , null=True , blank=True , max_length=100) #if any issue with slug try blank=true

    def save(self , *args , **kwargs):
        self.slug = generate_slug(self.event_name)
        super(Event , self).save(*args , **kwargs)

    def __str__(self):
        return self.event_name

class Event_workhand(models.Model):
    Workhand_category_id = models.ForeignKey('Workhand_category' , on_delete=models.CASCADE)
    number_of_workhand = models.IntegerField(default=11)
    price = models.DecimalField(max_digits=10, decimal_places=2 , default = None)
    event_id = models.ForeignKey('Event' , on_delete=models.CASCADE)

    def __str__(self):
        return self.Workhand_category_id.workhand_category_name
    
RATING = (
    (1,'1'),
    (2,'2'),
    (3,'3'),
    (4,'4'),
    (5,'5'),
)
class Event_Registrations(models.Model):
    registration_date = models.DateField(default=datetime.now)
    event_workhand_id = models.ForeignKey('Event_workhand' , on_delete=models.CASCADE , default=None)
    workhand_id = models.ForeignKey('Workhand',on_delete=models.CASCADE)
    registration_status = models.BooleanField(default=False)
    event_id = models.ForeignKey('Event' , on_delete=models.CASCADE)
    company_id = models.ForeignKey('Company' , on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING,default=0)
    payment_status = models.BooleanField(default=False)
    payment_date = models.DateField(default=datetime.now)
    

    def __str__(self):
        return self.event_id.event_name    


class Workhand_category(models.Model):
    workhand_category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.workhand_category_name   


class City(models.Model):
    city_name = models.CharField(max_length=255)
    state_id = models.ForeignKey('State' ,  on_delete=models.CASCADE)

    def __str__(self):
        return self.city_name
            
class State(models.Model):
    state_name = models.CharField(max_length=255)

    def __str__(self):
        return self.state_name
    

class Event_Category(models.Model):
    event_category = models.CharField(max_length=100)

    def __str__(self):
        return self.event_category 

class Event_subcategory(models.Model):
    Event_subcategory_name = models.CharField(max_length=100)
    Event_Category_id = models.ForeignKey('Event_Category' , on_delete=models.CASCADE)

    def __str__(self):
        return self.Event_subcategory_name
    

class Feedback(models.Model):
    feedback = models.TextField()
    feedback_date = models.DateField(default=datetime.now)
    event_id = models.ForeignKey('Event', on_delete=models.CASCADE)
    workhand_id = models.ForeignKey('Workhand', on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f"{self.workhand_id.first_name} ---> {self.event_id.event_name}"
    

# class Payment(models.Model):
#     workhand_id = models.ForeignKey('Workhand' , on_delete=models.CASCADE)
#     event_id = models.ForeignKey('Event' , on_delete=models.CASCADE)
#     company_id = models.ForeignKey('Company' , on_delete=models.CASCADE)
#     payment_status = models.BooleanField(default=False)
#     payment_date = models.DateField(default=datetime.now)

    
        

