from django.urls import path
from . import views

urlpatterns = [
    path('', views.listings, name='listings'),
    path('new', views.new, name='new_listing'),
    path('all', views.getListingAll, name = 'get_listings_all'),
    path('<slug:slug>/', views.listingDetailView.as_view(), name = "detail-view"),
]






