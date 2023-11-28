# Generated by Django 4.1.7 on 2023-11-28 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_data', '0004_alter_workhand_category_workhand_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='companyLogo_path',
            field=models.ImageField(default=None, null=True, upload_to='vendor_img/'),
        ),
        migrations.AlterField(
            model_name='workhand',
            name='profilePic_path',
            field=models.ImageField(default=None, null=True, upload_to='user_profile_img/'),
        ),
    ]
