# Generated by Django 3.2.23 on 2023-12-13 21:11

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0003_rename_user_post_owner'),
        ('likes', '0002_alter_like_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='like',
            old_name='user',
            new_name='owner',
        ),
        migrations.AlterUniqueTogether(
            name='like',
            unique_together={('post', 'owner')},
        ),
    ]
