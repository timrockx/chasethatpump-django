# Generated by Django 3.2.4 on 2021-07-11 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_full_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='fav_workout',
            new_name='location',
        ),
        migrations.AddField(
            model_name='profile',
            name='workout_style',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
