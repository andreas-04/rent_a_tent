# Generated by Django 3.2.4 on 2021-07-07 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_listing_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='catagory',
            field=models.CharField(blank=True, choices=[('Camping Equipment', 'Camping Equipment'), ('kyaks and Canoes', 'kyaks and Canoes'), ('Fishing Equipment', 'Fishing Equipment'), ('Sports Equipment', 'Sports Equipment'), ('Snow Sports Equipment', 'Snow Sports Equipment'), ('Other', 'Other')], max_length=21, null=True),
        ),
    ]
