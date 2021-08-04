from django.shortcuts import redirect, render
from . forms import ListingForm
from django.conf import settings
from home.models import Listing
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateView
# Create your views here.



class IndexView(TemplateView):

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['listing'] = Listing.objects.all()
        return context



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

class listingDetailView(DetailView):
    model = Listing
    template_name = "listing_detail.html"
#
#    def get_object(self, queryset=None):
#        return get_object_or_404(Listing, pk=self.kwargs.get('pk'))


#def categoryList(request, category_slug):
