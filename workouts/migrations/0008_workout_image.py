# Generated by Django 3.2.4 on 2021-07-02 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0007_auto_20210701_2024'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='workout_pics'),
        ),
    ]
