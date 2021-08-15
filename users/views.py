from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import generic
from users.models import Customer
from .forms import CustomerCreationForm


# Create your views here.

def home(request):
    return render(request, 'index.html')


class UserDetailView(generic.DetailView):
    model = User
    template_name = 'users/user_detail.html'


class CustomerDetailView(generic.DetailView):
    model = Customer


class CustomerCreationView(generic.edit.CreateView):
    form_class = CustomerCreationForm
    template_name = 'users/customer_form.html'


class CustomerUpdateView(generic.edit.UpdateView):
    form_class = CustomerCreationForm
    template_name = 'users/customer_form.html'


class CustomerDeleteView(generic.edit.DeleteView):
    form_class = CustomerCreationForm
    template_name = 'users/customer_form.html'
