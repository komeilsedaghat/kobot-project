# Generated by Django 4.0 on 2022-01-24 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0016_user_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile',
            field=models.ImageField(blank=True, upload_to='user/profile/'),
        ),
    ]
