# Generated by Django 4.1.7 on 2024-01-19 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_data', '0024_alter_event_registrations_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event_registrations',
            name='rating',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=0),
        ),
    ]
