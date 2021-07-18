from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator, MinValueValidator
# Create your models here.
listing_description_choices = (
        ("Camping Equipment", "Camping Equipment"),
        ("kayaks and Canoes", "kayaks and Canoes"),
        ('Fishing Equipment', "Fishing Equipment"),
        ('Sports Equipment', "Sports Equipment"),
        ('Snow Sports Equipment', "Snow Sports Equipment"),
        ('Other', "Other"),
        (None, 'Choose a Catagory')
    )

class Listing(models.Model):
    title = models.CharField(max_length=150)
    catagory = models.CharField(max_length=21, blank=True, null=True, choices = listing_description_choices)
    available_till = models.DateField('Available till')
    listing_imgs = models.ImageField(upload_to = 'images/')
    description = models.TextField(max_length=2000)
    pub_date = models.DateTimeField('Date published', auto_now = True)
    price_per_day = models.IntegerField(default=0)
#   images = models.ImageField //ADD AN IMAGE FIELD FOR MODEL
    def __str__(self):
        return self.title