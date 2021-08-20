from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import ParcelTrackForm
from .models import Parcel


# Create your views here.

class ParcelListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        return Parcel.objects.filter(booked_by=self.request.user)


class ParcelDetailView(LoginRequiredMixin, DetailView):
    model = Parcel


class ParcelCreateView(LoginRequiredMixin, CreateView):
    model = Parcel
    fields = ['type', 'city', 'street', 'zip', 'email', 'phone']

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        parcel = form.save(self)
        parcel.booked_by = request.user
        parcel.save()
        messages.success(request, 'Your parcel has been placed successfully')
        return redirect('parcels:parcels')


class ParcelUpdateView(UserPassesTestMixin, UpdateView):
    def test_func(self):
        return self.request.user == self.get_object().booked_by

    model = Parcel
    template_name = 'parcels/parcel_update.html'
    fields = ['type', 'city', 'street', 'zip', 'email', 'phone']


class ParcelDeleteView(UserPassesTestMixin, DeleteView):
    def test_func(self):
        return self.request.user == self.get_object().booked_by
    model = Parcel
    fields = ['type', 'city', 'street', 'zip', 'email', 'phone']
    # success_url = 'parcels:parcels'
    # fixme: having trouble here for success url


class ParcelTrackView(FormView):
    form_class = ParcelTrackForm
    template_name = 'parcels/parcel_track.html'

    def post(self, request, *args, **kwargs):
        try:
            parcel = Parcel.objects.get(pk=request.POST['parcel_id'])
            print(parcel)
            context = {
                "object": parcel,
            }
            return render(request, 'parcels/parcel_detail.html', context)
        except Exception as e:
            print(str(e))
            messages.error(request, 'Invalid parcel ID')
            return redirect('parcels:track')
