from django.urls import path
from parcels import views as parcel_view

app_name = 'parcels'

urlpatterns = [
    path('parcels/', parcel_view.ParcelListView.as_view(), name='parcels'),
    path('parcels/create/', parcel_view.ParcelCreateView.as_view(), name='create'),
    path('parcels/<int:pk>/', parcel_view.ParcelDetailView.as_view(), name='detail'),
]
