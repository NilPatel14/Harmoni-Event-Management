# Generated by Django 4.1.7 on 2023-12-26 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event_data', '0020_alter_event_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event_registrations',
            name='workhand_categoty_id',
        ),
        migrations.AddField(
            model_name='event_registrations',
            name='event_workhand_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='event_data.event_workhand'),
        ),
    ]