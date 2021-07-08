from django.shortcuts import render
from .forms import ListingForm
# Create your views here.
def listings(request):
    return render(request, 'listings.html')

def new(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
    else:
        form = ListingForm('ModelForm')
    return render(request, 'newlisting.html', {'form': form})
