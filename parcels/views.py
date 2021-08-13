from django.core.exceptions import ImproperlyConfigured
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Parcel


# Create your views here.


class BookParcel(CreateView):
    model = Parcel
    fields = ['parcel_type', 'receivers_email']

    def get_success_url(self):
        """Return the URL to redirect to after processing a valid form."""
        if self.success_url:
            url = self.success_url.format(**self.object.__dict__)
        else:
            try:
                url = self.object.get_absolute_url()
            except AttributeError:
                raise ImproperlyConfigured(
                    "No URL to redirect to.  Either provide a url or define"
                    " a get_absolute_url method on the Model.")
        return url
