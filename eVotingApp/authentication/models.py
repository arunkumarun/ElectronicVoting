from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfileInfo(models.Model):

    # Create relationship
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Adding extra attributes
    dob = models.DateField()
    citizenshipNumber = models.CharField(max_length=10, help_text='')
    address = models.TextField()
    mobileNumber = models.CharField(max_length=10, help_text='')
    drivingLicenseNo = models.TextField(blank=True)
    passportNo = models.TextField(blank=True)
    gender = models.TextField()

    def __str__(self):
        return self.user.username

class AdminInfo(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

