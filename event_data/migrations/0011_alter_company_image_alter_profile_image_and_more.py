# Generated by Django 4.1.7 on 2023-08-20 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_data', '0010_alter_company_image_alter_profile_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='image',
            field=models.ImageField(default=None, upload_to='vendor_img'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_img'),
        ),
        migrations.AlterField(
            model_name='service_provider',
            name='profile_img',
            field=models.ImageField(default=None, upload_to='user_profile_img'),
        ),
    ]
