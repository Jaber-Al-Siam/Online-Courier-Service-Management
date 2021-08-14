from django.shortcuts import render, redirect
from django.views import View
from users.forms import SignupForm
from django.contrib import messages
from django.contrib.auth import authenticate


# Create your views here.


def home(request):
    return render(request, 'index.html')


def viewOrUpdateProfile(request):
    return render(request, 'users/profile.html')


class UserCreationView(View):
    form_class = SignupForm
    template_name = 'registration/signup.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=raw_password)
            messages.success(request, 'Your account created successfully, please login')
            return redirect('login_page')
        else:
            form = self.form_class(request.POST)
            return render(request, self.template_name, {'form': form})
