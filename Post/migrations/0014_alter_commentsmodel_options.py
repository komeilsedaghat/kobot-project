# Generated by Django 4.0 on 2022-01-05 21:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0013_commentsmodel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='commentsmodel',
            options={'ordering': ['-created']},
        ),
    ]