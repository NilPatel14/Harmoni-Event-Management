# Generated by Django 4.1.7 on 2023-12-17 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_data', '0011_event_registrations_workhand_categoty_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='total_price',
            field=models.IntegerField(default=11),
        ),
    ]
