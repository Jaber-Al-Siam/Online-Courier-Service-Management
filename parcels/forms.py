from django import forms


class ParcelTrackForm(forms.Form):
    parcel_id = forms.IntegerField(required=True)


class CostCalculatorForm(forms.Form):
    AREA = [
        ('inside', 'Inside Dhaka'),
        ('outside', 'Outside Dhaka'),
    ]

    weight = forms.IntegerField(required=True)
    area = forms.ChoiceField(choices=AREA)
