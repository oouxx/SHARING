# Generated by Django 2.0 on 2018-11-29 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comm2hacker',
        ),
    ]
