from django.urls import path, reverse

from parcels import views as parcel_view

app_name = 'parcels'

urlpatterns = [
    path('parcels/', parcel_view.ParcelListView.as_view(), name='parcels'),
    path('parcels/<int:pk>/', parcel_view.ParcelDetailView.as_view(), name='detail'),
    path('parcels/create/', parcel_view.ParcelCreateView.as_view(), name='create'),
    path('parcels/<int:pk>/update', parcel_view.ParcelUpdateView.as_view(), name='update'),
    path('parcels/<int:pk>/delete', parcel_view.ParcelDeleteView.as_view(), name='delete'),
]
