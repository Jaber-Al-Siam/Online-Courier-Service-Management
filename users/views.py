from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import generic

from users.models import Customer
from .forms import CustomerCreationForm


# Create your views here.

def home(request):
    return render(request, 'index.html')


# fixme: think about the access of the views
# todo: access modifier


class UserDetailView(UserPassesTestMixin, generic.DetailView):
    def test_func(self):
        return True

    model = User
    template_name = 'users/user_detail.html'


class CustomerDetailView(UserPassesTestMixin, generic.DetailView):
    def test_func(self):
        return True

    model = Customer


class CustomerCreationView(generic.edit.CreateView):
    form_class = CustomerCreationForm
    template_name = 'users/customer_form.html'


class UserUpdateView(UserPassesTestMixin, generic.edit.UpdateView):
    def test_func(self: UserPassesTestMixin) -> bool:
        return True

    model = User
    fields = ['username', 'first_name', 'last_name', 'email', ]
    # form_class = CustomerCreationForm
    template_name = 'users/customer_update.html'


class CustomerUpdateView(UserPassesTestMixin, generic.edit.UpdateView):
    def test_func(self):
        return True

    model = Customer
    fields = ['first_name', 'last_name', 'phone', ]
    # form_class = CustomerCreationForm
    template_name = 'users/customer_update.html'


class CustomerDeleteView(UserPassesTestMixin, generic.edit.DeleteView):
    def test_func(self):
        return True

    form_class = CustomerCreationForm
    template_name = 'users/customer_form.html'
