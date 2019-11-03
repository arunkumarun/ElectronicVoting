# Creates user information fields to admin

from django import forms
from django.contrib.auth.models import User
from authentication.models import UserProfileInfo


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        for fieldname in ['username']:
            self.fields[fieldname].help_text = ""

    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('dob', 'citizenshipNumber', 'street','suburb','state','pincode', 'mobileNumber', 'drivingLicenseNo'
                  ,'passportNo','gender')

