# Generated by Django 4.1.7 on 2023-12-17 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_data', '0012_event_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='total_price',
            field=models.IntegerField(default=11, null=True),
        ),
    ]
