from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Parcel


# Create your views here.

class ParcelListView(ListView):
    def get_queryset(self):
        return Parcel.objects.filter(booked_by=self.request.user)


class ParcelDetailView(DetailView):
    model = Parcel


class ParcelCreateView(CreateView):
    model = Parcel
    fields = ['type', 'city', 'street', 'zip', 'email', 'phone']

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        parcel = form.save(self)
        parcel.booked_by = request.user
        parcel.save()
        messages.success(request, 'Your parcel has been placed successfully')
        return redirect('parcels:parcels')


class ParcelUpdateView(UpdateView):
    model = Parcel
    template_name = 'parcels/parcel_update.html'
    fields = ['type', 'city', 'street', 'zip', 'email', 'phone']


class ParcelDeleteView(DeleteView):
    model = Parcel
    fields = ['type', 'city', 'street', 'zip', 'email', 'phone']
    # success_url = 'parcels:parcels'
