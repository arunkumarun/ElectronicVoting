from django.db import models


# Create your models here.
class Party(models.Model):
    party_name = models.CharField(max_length=50, default='')
    party_logo = models.ImageField(upload_to='media/', default='/media/UAP.jpg')

    def __str__(self):
        return self.party_name

class Candidate(models.Model):
    party = models.OneToOneField(Party, on_delete=models.CASCADE)

    candidate_surname = models.CharField(max_length=50, default='')
    candidate_givenname = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.candidate_givenname+" "+self.candidate_surname

class PartyPreference(models.Model):
    # party = models.OneToOneField(Party, on_delete=models.CASCADE)
    party_name = models.CharField(max_length=50, default='')
    party_preference = models.IntegerField(default='')


class CandidatePreference(models.Model):
    # candidate = models.OneToOneField(Candidate, on_delete=models.CASCADE)
    candidate_surname = models.CharField(max_length=50, default='')
    candidate_preference = models.IntegerField(default='')


class ElectionDetails(models.Model):
    election_date = models.DateField(help_text="Please use the following format: YYYY-MM-DD")

    start_time = models.TimeField(blank=True)
    end_time = models.TimeField(blank=True)
