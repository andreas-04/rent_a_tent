# Generated by Django 3.2.4 on 2021-07-17 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_listing_listing_imgs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='listing_imgs',
            field=models.ImageField(default=True, upload_to='images/'),
            preserve_default=False,
        ),
    ]
