# Generated by Django 2.0 on 2018-11-26 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20181126_1126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='softwaredetail',
            name='type',
        ),
        migrations.AddField(
            model_name='software',
            name='type',
            field=models.CharField(choices=[('', ''), ('Windows', 'Windows'), ('Android', 'Android'), ('IOS', 'IOS'), ('MAC', 'MAC'), ('Linux', 'Linux')], default='', max_length=10, verbose_name='软件分类'),
        ),
    ]
