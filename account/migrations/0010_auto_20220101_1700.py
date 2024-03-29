# Generated by Django 3.2.7 on 2022-01-01 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_auto_20220101_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blockandreportmodel',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='blockandreportmodel',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_report', to='account.user'),
        ),
    ]
