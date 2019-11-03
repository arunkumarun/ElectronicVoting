# Django Admin functionality

from django.contrib import admin
from election.models import Party,Candidate,ElectionDetails
# Register your models here.

# Register Party information to admin page
admin.site.register(Party)
# Register Candidate information to admin page
admin.site.register(Candidate)
# Register the election details to admin page
admin.site.register(ElectionDetails)