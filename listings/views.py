from django.shortcuts import redirect, render
from . forms import ListingForm
from django.conf import settings
# Create your views here.
def listings(request):
    return render(request, 'listings.html')

def new(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        if request.method == 'POST':
            form = ListingForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('homepage')

        else:
            form = ListingForm()
        return render(request, 'newlisting.html', {'form': form})
