from django import forms


class ParcelTrackForm(forms.Form):
    parcel_id = forms.IntegerField(required=True)
