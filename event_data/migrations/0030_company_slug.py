# Generated by Django 4.1.7 on 2024-02-04 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_data', '0029_alter_workhand_avg_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
