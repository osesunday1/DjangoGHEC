from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User








class User(AbstractUser):

    is_client = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)


    email = models.EmailField(unique=True, null=False)
    username= models.CharField(max_length=100)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS= ['username']

    def __str__(self):
        return self.username




class Client (models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        self.user.first_name = self.first_name  # Set the username to the first name of the client
        self.user.last_name= self.last_name
        self.user.save()  # Save the updated user instance
        super(Client, self).save(*args, **kwargs)  # Save the client instance

    def delete(self, *args, **kwargs):
        self.user.delete()
        return super(self.__class__, self).delete(*args, **kwargs)

    def __str__(self):
        return self.first_name
    


class Admin (models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def delete(self, *args, **kwargs):
        self.user.delete()
        return super(self.__class__, self).delete(*args, **kwargs)

    def __str__(self):
        return self.first_name
    


Package_Type = [ 
    ('Canada Schooling','Canada Schooling' ),
    ('Canada Express Entry','Canada Express Entry' ),
    ('Canada Tourism','Canada Tourism' ),
    ('Canada Business','Canada Business' ),

    ('USA Schooling','USA Schooling' ),
    ('USA Express Entry','USA Express Entry' ),
    ('USA Tourism','USA Tourism' ),
    ('USA Business','USA Business' ),
    ('USA Birth Services','USA Birth Services' ),

    ('Brazil Birth Services','Brazil Birth Services' ),

    ('Barbados Birth Services','Barbados Birth Services' ),

    ('Turkey Schooling','Turkey Schooling' ),
    ('Turkey Tourism','Turkey Tourism' ),
    ('Turkey Business','Turkey Business' ),

                   ]


Country_Type= [
    ('Brazil','Brazil' ),
    ('Canada','Canada' ),
    ('Turkey','Turkey' ),
    ('USA','USA' ),
]

class Application (models.Model):
    client_name = models.ForeignKey(User, null=True, on_delete= models.SET_NULL)
    country = models.CharField(choices=Country_Type,max_length=120, null= True, blank= True)
    package = models.CharField(choices=Package_Type,max_length=120, null= True, blank= True)
    processing_fee=  models.CharField( max_length=120, null= True, blank= True)
    amount_paid=  models.CharField( max_length=120, null= True, blank= True)
    debt=  models.CharField( max_length=120, null= True, blank= True)
    date_created= models.DateField(auto_now_add=True)
    ielts = models.BooleanField(default=False)
   

    def __str__(self):
        return self.client_name
    

class Receipt (models.Model):
    client_name = models.ForeignKey(User, null=True, on_delete= models.SET_NULL)
    amount_paid = models.CharField(max_length=120, null= True, blank= True)
    date_paid= models.DateField()
    sender_name= models.CharField(max_length=100)
    bank_name= models.CharField(max_length=100)
    reason = models.CharField(choices=Package_Type,max_length=120, null= True, blank= True)

    def __str__(self):
        return self.client_name
    
