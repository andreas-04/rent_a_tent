from django.db import models

# Create your models here.
class Listing(models.Model):
    listing_description_choices = (
        ("Camping Equipment", "Camping Equipment"),
        ("kayaks and Canoes", "kayaks and Canoes"),
        ('Fishing Equipment', "Fishing Equipment"),
        ('Sports Equipment', "Sports Equipment"),
        ('Snow Sports Equipment', "Snow Sports Equipment"),
        ('Other', "Other"),
        (None, 'Choose a Catagory')
    )
    title = models.CharField(max_length=150)
    catagory = models.CharField(max_length=21, blank=True, null=True, choices = listing_description_choices)
    description = models.TextField(max_length=2000)
#   images = models.ImageField //ADD AN IMAGE FIELD FOR MODEL
    def __str__(self):
        return self.title