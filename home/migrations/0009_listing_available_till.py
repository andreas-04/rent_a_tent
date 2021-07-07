# Generated by Django 3.2.4 on 2021-07-07 23:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20210707_2148'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='available_till',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Available till'),
            preserve_default=False,
        ),
    ]
