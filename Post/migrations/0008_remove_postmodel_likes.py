# Generated by Django 3.2.7 on 2021-12-14 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0007_postmodel_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postmodel',
            name='likes',
        ),
    ]
