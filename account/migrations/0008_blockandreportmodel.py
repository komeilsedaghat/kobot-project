# Generated by Django 3.2.7 on 2022-01-01 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_alter_user_blocked_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlockAndReportModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_text', models.CharField(blank=True, max_length=400)),
                ('number_reported', models.PositiveSmallIntegerField()),
                ('status', models.BooleanField(default=False)),
                ('user', models.ManyToManyField(blank=True, to='account.User')),
            ],
        ),
    ]