# Generated by Django 3.2.4 on 2021-08-01 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_alter_listing_listing_imgs'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
