# Modelling user interface and admin interface
from django.db import models
from django.contrib.auth.models import User


# Create UserProfileInfo models here.
class UserProfileInfo(models.Model):

    # Create relationship
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Including additional user  attributes
    dob = models.DateField(help_text = "Please use the following format: YYYY-MM-DD")
    citizenshipNumber = models.CharField(max_length=10, help_text="Enter your 10 digit citizenship Number")
    street = models.CharField(max_length=30 , default ='')
    suburb = models.CharField(max_length=30,default ='')
    STATES = (('NSW','New South Wales'),('WA','Western Australia'),('SA','South Australia'),('TAS','Tasmania'),
              ('VIC','Victoria'),('QLD','Queensland'))
    state = models.CharField(max_length=20, choices=STATES, default = 'Select State')
    pincode = models.IntegerField(default = '')
    mobileNumber = models.CharField(max_length=10, help_text='')
    drivingLicenseNo = models.CharField(max_length=10,blank=True)
    passportNo = models.CharField(max_length=20,blank=True)
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'), ('U', 'Unspecified'))
    #EVIDENCES = (('DL','Driving License') , ('P','Passport'))
    #evidence = models.CharField(max_length = 10, choices = EVIDENCES, default='DL',
                                #help_text = "Choose Identification Document")
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default = 'Unspecified',
                                    help_text = "Select Gender")
    voted = models.BooleanField(default=False)
    def __str__(self):
        return self.user.username

# Creates AdminInfo models here.
class AdminInfo(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

