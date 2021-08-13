from django.urls import path
from .views import BookParcel

urlpatterns = [
    path('parcel/', BookParcel.as_view(), name='book_parcel_page')
]