from django.contrib import admin
from authentication.models import UserProfileInfo, AdminInfo

# Register your models here.


admin.site.register(UserProfileInfo)
admin.site.register(AdminInfo)
