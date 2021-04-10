from django.shortcuts import render

# Create your views here.

def home_action(request):
    return render(request, 'education/home.html')