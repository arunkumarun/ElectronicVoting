from django.contrib import admin
from election.models import Party,Candidate,ElectionDetails
# Register your models here.

admin.site.register(Party)
admin.site.register(Candidate)
admin.site.register(ElectionDetails)