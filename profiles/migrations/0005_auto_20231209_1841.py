# Generated by Django 3.2.23 on 2023-12-09 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20231209_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='cover_photo',
            field=models.ImageField(default='images/default_profile_ifketo.jpg', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(default='images/default_profile_yansvo.jpg', upload_to='images/'),
        ),
    ]
