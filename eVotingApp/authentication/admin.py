# Creates admin information

from django.contrib import admin
from authentication.models import UserProfileInfo, AdminInfo

# Registers UserProfileInfo model to admin
# Registers admin information in AdminInfo model


admin.site.register(UserProfileInfo)
admin.site.register(AdminInfo)
