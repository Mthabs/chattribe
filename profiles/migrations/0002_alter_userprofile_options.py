# Generated by Django 3.2.23 on 2023-12-13 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'ordering': ['-created_at']},
        ),
    ]
