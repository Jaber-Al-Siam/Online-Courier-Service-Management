from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView
from .models import Parcel


# Create your views here.

class ListView(ListView):
    def get_queryset(self):
        return Parcel.objects.all()


class DetailView(DetailView):
    model = Parcel


class ParcelBook(CreateView):
    model = Parcel
    fields = ['parcel_type', 'receiver_email', 'receiver_phone']

