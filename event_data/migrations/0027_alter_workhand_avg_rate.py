# Generated by Django 4.1.7 on 2024-01-19 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_data', '0026_workhand_avg_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workhand',
            name='avg_rate',
            field=models.IntegerField(default=0),
        ),
    ]