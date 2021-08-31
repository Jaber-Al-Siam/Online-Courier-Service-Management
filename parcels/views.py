from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import ParcelTrackForm, CostCalculatorForm
from .models import Parcel


# Create your views here.

def cost_calculator(request):
    return render(request, 'cost_calculator.html')


class CostCalculatorView(FormView):
    form_class = CostCalculatorForm
    template_name = 'parcels/cost_calculator.html'

    def post(self, request, *args, **kwargs):
        if request.POST['weight'] == '0':
            messages.error(request, 'Weight cannot be 0')
            return redirect('parcels:cost_calculator')
        unit_price = 15.0
        minimum_cost = 60.0
        if request.POST['area'] == 'outside':
            unit_price = 30.0
            minimum_cost = 120.0

        charge = max(minimum_cost, unit_price * float(request.POST['weight']))
        messages.success(request, f'Estimated shipping cost is {charge} taka')
        return redirect('parcels:cost_calculator')


class ParcelListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        return Parcel.objects.filter(booked_by=self.request.user)


class ParcelDetailView(LoginRequiredMixin, DetailView):
    model = Parcel

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return render(request, 'parcels/' + self.object.status + '.html', context)


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
            return redirect('parcels:detail', pk=parcel.pk)
        except Exception as e:
            print(str(e))
            messages.error(request, 'Invalid parcel ID')
            return redirect('parcels:track')
