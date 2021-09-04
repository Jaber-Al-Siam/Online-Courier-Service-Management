from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import ParcelTrackForm, CostCalculatorForm, AddressForm, ReceiverForm, ParcelForm
from .models import Parcel, Address


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


class ParcelDetailView(DetailView):
    model = Parcel

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return render(request, 'parcels/' + self.object.status + '.html', context)


class ParcelCreateView(LoginRequiredMixin, CreateView):
    model = Parcel
    fields = ['type', ]
    template_name = 'parcels/parcel_form.html'

    def get(self, request, *args, **kwargs):
        parcel_form = self.get_form()
        pickup_address_form = AddressForm()
        receiver_address_form = AddressForm()
        receiver_form = ReceiverForm()
        context = {
            'parcel_form': parcel_form,
            'pickup_address_form': pickup_address_form,
            'receiver_form': receiver_form,
            'receiver_address_form': receiver_address_form,
        }
        return render(request=request, template_name=self.get_template_names(), context=context)

    def post(self, request, *args, **kwargs):
        parcel = ParcelForm(request.POST).save()
        pickup_address = Address(country=request.POST.getlist('country')[0], city=request.POST.getlist('city')[0],
                                 street=request.POST.getlist('street')[0], zip=request.POST.getlist('zip')[0])
        pickup_address.save()
        receiver_address = Address(country=request.POST.getlist('country')[1], city=request.POST.getlist('city')[1],
                                   street=request.POST.getlist('street')[1], zip=request.POST.getlist('zip')[1])
        receiver_address.save()

        receiver = ReceiverForm(request.POST).save()
        receiver.address = receiver_address
        receiver.save()
        parcel.pickup_address = pickup_address
        parcel.receiver = receiver
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
