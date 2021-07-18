from typing import List
from django import forms
from django.db.models import fields
from django.forms import ModelForm
from django.db import models
from home.models import Listing

class DateInput(forms.DateInput):
    input_type = 'date'


class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = [
        'title', 
        'catagory', 
        'available_till',
        'listing_imgs',
        'description',
        'price_per_day',
        ]
        widgets = {
            'available_till': DateInput()
        }