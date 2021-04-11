from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User



DEMO_CHOICES =(
    ("1", "Science"),
    ("2", "Math"),
    ("3", "History"),
    ("4", "English"),
)

VOLUME_CHOICES =(
    ("1", "loud"),
    ("2", "medium"),
    ("3", "quiet"),
)
class MeetPeopleForm(forms.Form):
    age = forms.IntegerField()
    volume = forms.MultipleChoiceField(choices = VOLUME_CHOICES)
    location = forms.CharField(max_length=200)
    study_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    study_period = forms.CharField(max_length=200)
    subject = forms.MultipleChoiceField(choices = DEMO_CHOICES)

class login_form(forms.Form):

    username = forms.CharField(max_length = 100)
    password = forms.CharField(max_length = 100, widget = forms.PasswordInput())

    def clean(self):
        # dictionary of usernames and passwords
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        user = authenticate(username = username, password = password)
        if (not user):
            raise forms.ValidationError("Invalid username/password")

        return cleaned_data

class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=20)
    last_name  = forms.CharField(max_length=20)
    email = forms.CharField(max_length=50,
                                 widget = forms.EmailInput())
    username = forms.CharField(max_length = 20)
    password = forms.CharField(max_length = 200,
                                 label='Password',
                                 widget = forms.PasswordInput())
    confirm_password  = forms.CharField(max_length = 200,
                                 label='Confirm Password',
                                 widget = forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        username = cleaned_data.get('username')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords did not match.")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Account with username already exists.")
        return cleaned_data
