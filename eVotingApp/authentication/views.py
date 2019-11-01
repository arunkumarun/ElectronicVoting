from django.shortcuts import render
from authentication.forms import UserForm, UserProfileInfoForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

import logging


# Create your views here.
from election.models import ElectionDetails,Party,Candidate


log = logging.getLogger("MYAPP")


def index(request):
    return render(request, 'authentication/index.html')


@login_required
def home(request):
    election = ElectionDetails.objects.all()
    context = {
        'election': election
    }
    return render(request, 'user/home.html', context)

@login_required
def voting(request):
    party = Party.objects.all()
    candidate = Candidate.objects.all()
    print("Voting Page")
    print(party)
    print(candidate)
    context = {
        'party' : party,
        'candidate' : candidate
    }
    return render(request, 'user/voting.html', context)
@login_required
def instruction(request):
    return render(request, 'user/instruction.html',{})

def voting(request):
    return  render(request,'user/voting.html',{})

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
