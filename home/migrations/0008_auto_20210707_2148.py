# Generated by Django 3.2.4 on 2021-07-07 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20210707_2131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='final_rent_date',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='init_rent_date',
        ),
        migrations.AddField(
            model_name='listing',
            name='pub_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Date published'),
        ),
    ]
