from django.shortcuts import render
from authentication.forms import UserForm, UserProfileInfoForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

import logging


# Create your views here.
from election.models import ElectionDetails, Party, Candidate, CandidatePreference, PartyPreference
from authentication.models import UserProfileInfo

log = logging.getLogger("MYAPP")


def index(request):
    return render(request, 'authentication/index.html')


@login_required
def home(request):
    election = ElectionDetails.objects.all()
    userId = request.user.id
    userProfileInfoQuery = UserProfileInfo.objects.filter(user_id=userId)
    if len(userProfileInfoQuery) > 0:
        userProfileInfo = userProfileInfoQuery[0]
    context = {
        'election': election,
        'userProfileInfo': userProfileInfo
    }
    return render(request, 'user/home.html', context)


@login_required
def voting(request):
    party = Party.objects.all()
    candidate = Candidate.objects.all()
    context = {
        'party' : party,
        'candidate' : candidate
    }
    return render(request, 'user/voting.html', context)


@login_required
def partyvote(request):
    userId = request.user.id
    userProfile = UserProfileInfo.objects.filter(user_id=userId)
    userProfile.update(voted=True)

    if request.method == "POST":
        party = Party.objects.all()
        for p in party:
            party_pref = PartyPreference()
            party_pref.party_name = p.party_name
            party_pref.party_preference = request.POST.get(p.party_name)
            party_pref.save()
    log.info("USER Voted "+ request.user.username)
    return render(request, 'user/thanksforvoting.html',{})


@login_required
def candidatevote(request):
    userId = request.user.id
    userProfile = UserProfileInfo.objects.filter(user_id=userId)
    userProfile.update(voted=True)

    if request.method == "POST":
        candidate = Candidate.objects.all()
        for c in candidate:
            cand_pref = CandidatePreference()
            cand_pref.candidate_surname = c.candidate_surname
            cand_pref.candidate_preference=request.POST.get(c.candidate_surname)
            cand_pref.save()
    log.info("USER Voted "+ request.user.username)
    return render(request, 'user/thanksforvoting.html',{})


@login_required
def instruction(request):
    return render(request, 'user/instruction.html',{})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()
            log.info("NEW USER REGISTERED "+ user.username)
            registered = True
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'authentication/registration.html', {'user_form': user_form,
                                                                'profile_form': profile_form,
                                                                'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                log.info("USER LOGGED IN " + username)
                return HttpResponseRedirect(reverse('home'))

            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("someone tried to login and failed!")
            # print("Username: {} and password {}".format(username, password))
            return HttpResponse("invalid login details supplied!")
    else:
        return render(request, 'authentication/login.html', {})
