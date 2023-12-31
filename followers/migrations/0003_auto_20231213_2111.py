# Generated by Django 3.2.23 on 2023-12-13 21:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('followers', '0002_auto_20231212_1701'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follower',
            old_name='user',
            new_name='owner',
        ),
        migrations.AlterField(
            model_name='follower',
            name='followed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followed', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='follower',
            unique_together={('owner', 'followed')},
        ),
    ]
