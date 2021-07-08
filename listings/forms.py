from typing import List
from django import forms
from django.db.models import fields
from django.forms import ModelForm
from django.db import models
from home.models import Listing

#listing_description_choices = (
#        ("Camping Equipment", "Camping Equipment"),
#        ("kayaks and Canoes", "kayaks and Canoes"),
#        ('Fishing Equipment', "Fishing Equipment"),
#        ('Sports Equipment', "Sports Equipment"),
#        ('Snow Sports Equipment', "Snow Sports Equipment"),
#        ('Other', "Other"),
#        (None, 'Choose a Catagory')
#)




class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = [
        'title', 
        'catagory', 
        'available_till',
        'description',
        ]
