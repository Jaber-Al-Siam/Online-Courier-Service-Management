from django.urls import path
from parcels import views as parcel_view

app_name = 'parcels'

urlpatterns = [
    path('parcels/', parcel_view.ListView.as_view(), name='parcel'),
    path('parcels/create/', parcel_view.ParcelBook.as_view(), name='create'),
    path('parcels/<int:pk>/', parcel_view.DetailView.as_view(), name='detail'),
]
