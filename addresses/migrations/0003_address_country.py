# Generated by Django 3.0.5 on 2020-04-22 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0002_auto_20200422_0450'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='country',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
