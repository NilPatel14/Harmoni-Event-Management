# Generated by Django 4.1.7 on 2024-01-19 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_data', '0025_alter_event_registrations_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='workhand',
            name='avg_rate',
            field=models.IntegerField(default=0, max_length=5),
        ),
    ]
