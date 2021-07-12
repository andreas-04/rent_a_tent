from django.shortcuts import redirect, render
from . forms import ListingForm
# Create your views here.
def listings(request):
    return render(request, 'listings.html')

def new(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')

    else:
        form = ListingForm()
    return render(request, 'newlisting.html', {'form': form})
