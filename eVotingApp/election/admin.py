from django.contrib import admin
from election.models import Party,Candidate
# Register your models here.

admin.site.register(Party)
admin.site.register(Candidate)