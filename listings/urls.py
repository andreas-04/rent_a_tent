from django.urls import path
from . import views

urlpatterns = [
    path('', views.listings, name='listings'),
    path('new', views.new, name='new_listing')
]