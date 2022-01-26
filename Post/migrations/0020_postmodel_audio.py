# Generated by Django 4.0 on 2022-01-26 17:57

import Post.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0019_alter_postmodel_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='audio',
            field=models.FileField(blank=True, upload_to='audio/', validators=[Post.models.audio_size]),
        ),
    ]