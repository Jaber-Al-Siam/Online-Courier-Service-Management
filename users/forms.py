from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Customer


class CustomerCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    phone = forms.CharField(max_length=200)

    class Meta:
        model = Customer
        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'password1', 'password2', ]
