# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


# to store the user data(registration data)
class CustomUser(AbstractUser):
    name = models.CharField(max_length=100)

    # Remove the custom related_name and use the default ones
    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        related_name='customuser_set',
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_name='customuser_set',
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )

class Profile(models.Model):
    user = models.OneToOneField(CustomUser , on_delete=models.CASCADE)
    forget_password_token = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)




# Employer_Profile details

class Employer_Profile(models.Model):
    employer_id = models.AutoField(primary_key=True)
    employer_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=30)
    #federal_employer_identification_number = models.CharField(max_length=50)
    street_name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    number_of_employees = models.IntegerField()
    department = models.CharField(max_length=50)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.employer_name

# class Employee_Details(models.Model):
#     employer_id=models.IntegerField(max_length=20)
#     employee_id = models.AutoField(primary_key=True)
#     email = models.EmailField()                                #here the employee email
#     empcode = models.CharField(max_length=20, unique=True)     #added later on to fetch the email via empcode
#     employee_name = models.CharField(max_length=50)
#     #garnishment_fees  = models.FloatField(max_length=50)    #no need
#     net_pay=  models.FloatField()
#     minimun_wages=  models.CharField(max_length=50)
#     pay_cycle=models.FloatField()
#     #number_of_garnishment= models.CharField(max_length=50)    #no need
#     location =models.CharField(max_length=50)

class Employee_Details(models.Model):
    emp_code=models.CharField(max_length=20,primary_key=True, unique=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)     #added later on to fetch the email via empcode
    emp_role = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    emp_address =models.CharField(max_length=100)
    status = models.CharField(max_length=25)


  
# class Email_Data(models.Model):                                      #email table
#       empcode = models.IntegerField(max_length=20)
#       email = models.EmailField(50)
#       name = models.CharField(max_length=50)

#       def __str__(self):
#         return self.name
#     tax_id = models.AutoField(primary_key=True)
#     employee_id=models.IntegerField(max_length=20)
#     fedral_income_tax =models.FloatField()
#     social_and_security =models.FloatField()
#     medicare_tax= models.FloatField()
#     state_taxes =models.FloatField()

#TABLE EMAIL CONTAIN email and empcode, we will take user 
#email from this table to trigger mail
# class Email(models.Model):
#     empcode = models.CharField(max_length=20, unique=True)
#     email = models.EmailField()

#     def __str__(self):
#         return self.email

#COUNT DATA TABLE 
from django.db import models

class count_number(models.Model):
    empcode = models.CharField(max_length=255)
    intime = models.CharField(max_length=255, null=True, blank=True)
    outtime = models.CharField(max_length=255, null=True, blank=True)
    worktime = models.CharField(max_length=255, null=True, blank=True)
    overtime = models.CharField(max_length=255, null=True, blank=True)
    breaktime = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    datestring = models.CharField(max_length=255)
    remark = models.CharField(max_length=255, null=True, blank=True)
    erl_out = models.CharField(max_length=255, null=True, blank=True)
    late_in = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)

