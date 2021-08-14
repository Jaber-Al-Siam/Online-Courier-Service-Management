from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView
from .models import Parcel


# Create your views here.

class ParcelListView(ListView):
    def get_queryset(self):
        return Parcel.objects.all()


class ParcelDetailView(DetailView):
    model = Parcel


class ParcelCreateView(CreateView):
    model = Parcel
    fields = ['type', 'city', 'street', 'zip', 'email', 'phone']
