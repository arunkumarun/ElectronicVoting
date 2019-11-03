# Models creates the table.
# Create your models here.
from django.db import models


# Model for creating Party Table
class Party(models.Model):
    party_name = models.CharField(max_length=50, default='')
    party_logo = models.ImageField(upload_to='media/', default='/media/UAP.jpg')

# Returns Party created to the Party Table
    def __str__(self):
        return self.party_name


# Model for creating Candidate Table
class Candidate(models.Model):
    party = models.OneToOneField(Party, on_delete=models.CASCADE)

    candidate_surname = models.CharField(max_length=50, default='')
    candidate_givenname = models.CharField(max_length=50, default='')

# Returns the Candidate created to the table
    def __str__(self):
        return self.candidate_givenname+" "+self.candidate_surname


# Model for Party Preference Table
class PartyPreference(models.Model):
    # party = models.OneToOneField(Party, on_delete=models.CASCADE)
    party_name = models.CharField(max_length=50, default='')
    party_preference = models.IntegerField(default='')


# Model for Candidate Preference Table
class CandidatePreference(models.Model):
    # candidate = models.OneToOneField(Candidate, on_delete=models.CASCADE)
    candidate_surname = models.CharField(max_length=50, default='')
    candidate_preference = models.IntegerField(default='')


# Model for Election Details Table
class ElectionDetails(models.Model):
    election_date = models.DateField(help_text="Please use the following format: YYYY-MM-DD")

    start_time = models.TimeField(blank=True)
    end_time = models.TimeField(blank=True)
