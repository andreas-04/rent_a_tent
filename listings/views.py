from django.shortcuts import redirect, render
from . forms import ListingForm
from django.conf import settings
from home.models import Listing
# Create your views here.
def listings(request):
    return render(request, 'listings.html')

def new(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        if request.method == 'POST':
            form = ListingForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('homepage')

        else:
            form = ListingForm()
        return render(request, 'new.html', {'form': form})



def getListingAll(request):
    listing = Listing.objects.all
    return render(request, 'all.html', {"listing":listing} )

