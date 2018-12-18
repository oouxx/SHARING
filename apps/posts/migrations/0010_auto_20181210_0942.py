# Generated by Django 2.0 on 2018-12-10 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_auto_20181205_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='opensource',
            name='url',
            field=models.CharField(default='/opensource/details/', max_length=100, verbose_name='详情页面路由'),
        ),
        migrations.AddField(
            model_name='programming',
            name='url',
            field=models.CharField(default='/program/details/', max_length=100, verbose_name='详情页面路由'),
        ),
        migrations.AlterField(
            model_name='software',
            name='url',
            field=models.CharField(default='/software/details/', max_length=100, verbose_name='详情页面路由'),
        ),
    ]