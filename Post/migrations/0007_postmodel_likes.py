# Generated by Django 3.2.7 on 2021-12-14 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20211209_0746'),
        ('Post', '0006_delete_likepostmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='likes',
            field=models.ManyToManyField(related_name='like', to='account.User'),
        ),
    ]
