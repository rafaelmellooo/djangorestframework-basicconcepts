# Generated by Django 3.0.5 on 2020-04-22 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attractions', '0001_initial'),
        ('touristattractions', '0002_auto_20200421_2329'),
    ]

    operations = [
        migrations.AddField(
            model_name='touristattraction',
            name='attractions',
            field=models.ManyToManyField(to='attractions.Attraction'),
        ),
    ]