from django import forms

from parcels.models import Parcel, Address, Receiver


class ParcelTrackForm(forms.Form):
    parcel_id = forms.IntegerField()


class CostCalculatorForm(forms.Form):
    AREA = [
        ('inside', 'Inside Dhaka'),
        ('outside', 'Outside Dhaka'),
    ]

    weight = forms.IntegerField()
    area = forms.ChoiceField(choices=AREA)


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'


class ReceiverForm(forms.ModelForm):
    class Meta:
        model = Receiver
        exclude = ['address']


class ParcelForm(forms.ModelForm):
    class Meta:
        model = Parcel
        fields = ['type', ]
