
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from django.shortcuts import render, reverse, redirect

# Create your views here.
from django.views.decorators.csrf import ensure_csrf_cookie

from education.templates.education.forms import MeetPeopleForm, login_form, RegisterForm

from education.models import Profile


@ensure_csrf_cookie

def matching_algorithm(request, age, volume, location, study_period, study_time, subject):
    best_student = Profile.objects.get(username = request.user.username)
    max_points = 0
    for profile in Profile.objects.all():
        points = 0
        if(profile.age == age):
            points = points + 1
        if(profile.volume == volume):
            points = points + 1
        if(profile.location == location):
            points = points + 1
        if(profile.study_period == study_period):
            points = points + 1
        if(profile.study_time == study_time):
            points = points + 1
        if(profile.subject == subject):
            points = points + 1
        if(points > max_points):
            max_points = points
            best_student = profile
    print("best student")
    print(best_student.username)
    return best_student.username

def home_action(request):
    return render(request, 'education/home.html')



@ensure_csrf_cookie
def login_action(request):
    if (request.method == 'GET'):
        context = {
            'form': login_form(),
            'username': ""
        }
        return render(request, 'education/login.html', context)

    if (request.method == 'POST'):
        print('ENTERED')
        form = login_form(request.POST)
        username = form['username'].data
        password = form['password'].data
        context = {
            'form': form,
            'username': username
        }

        if (not form.is_valid()):
            return render(request, 'education/login.html', context)

        new_user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])

        login(request, new_user)
        context = {
            'form': MeetPeopleForm(),
            'username': username
        }
        print(username)
        return redirect('match')
        #return render(request, 'education/match.html', context)

@ensure_csrf_cookie
def register_action(request):

    for user in User.objects.all():
        print(user.first_name + " " + user.last_name)

    for user in Profile.objects.all():
        print(user.username)

    print("whaat")
    print(Profile.objects.all().count())

    if (request.method == 'GET'):
        context = {'form': RegisterForm()}
        return render(request, 'education/register.html', context)

    form = RegisterForm(request.POST)
    context = {
        'form': form,
    }

    if not form.is_valid():
        return render(request, 'education/register.html', context)

    new_user = User.objects.create_user(username=form.cleaned_data['username'],
                                        password=form.cleaned_data['password'],
                                        email=form.cleaned_data['email'],
                                        first_name=form.cleaned_data['first_name'],
                                        last_name=form.cleaned_data['last_name'])
    new_user.save()

    new_profile = Profile(first_name=form.cleaned_data['first_name'],
                          last_name=form.cleaned_data['last_name'],
                          username = form.cleaned_data['username'])
    new_profile.save()
    print("whaat")
    print(Profile.objects.all().count())



    new_user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])

    login(request, new_user)
    context = {
        'username': request.user.username,
        'form': MeetPeopleForm()
    }
    return redirect('match')

def match_action(request):
    print(request.user.username)
    if (request.method == 'GET'):
        context = {
            'form': MeetPeopleForm()
        }
        return render(request, 'education/match.html', context)

    if (request.method == 'POST'):
        form = MeetPeopleForm(request.POST)
        age = form['age'].data
        volume = form['volume'].data
        location = form['location'].data
        study_period = form['study_period'].data
        study_time = form['study_time'].data
        subject = form['subject'].data
        best_match = matching_algorithm(request, age, volume, location, study_period, study_time, subject)
        context = {
            'form': form,
            'best_match': best_match
        }

        for profile in Profile.objects.all():
            print(profile.username)
            if profile.username == request.user.username:
                profile.age = age
                profile.volume = volume
                profile.location = location
                profile.study_period = study_period
                profile.study_time = study_time
                profile.subject = subject
                profile.save()

        if (not form.is_valid()):
            return render(request, 'education/match.html', context)

    return render(request, 'education/viewmatches.html', context)

def viewmatches_action(request):
    print("ENTERED")
    for profile in Profile.objects.all():
        print('HERE')
        print(profile.username)
        print(profile.age)
    return render(request, 'education/viewmatches.html')

def cafe_action(request):
    return render(request, 'education/cafes.html')

def chat_action(request):
    return render(request, 'education/chat.html')


