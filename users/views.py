from django.shortcuts import render


# Create your views here.


def home(request):
    return render(request, 'index.html')


def signup(request):
    return render(request, 'users/signup.html')


def viewOrUpdateProfile(request):
    return render(request, 'users/profile.html')
