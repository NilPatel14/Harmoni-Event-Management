# Generated by Django 4.1.7 on 2023-11-26 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_data', '0003_event_event_subcategory_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workhand_category',
            name='workhand_category_name',
            field=models.CharField(max_length=50),
        ),
    ]
