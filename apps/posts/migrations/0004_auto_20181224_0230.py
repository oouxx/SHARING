# Generated by Django 2.0.8 on 2018-12-24 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20181224_0222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=None, max_length=100, verbose_name='子模型名'),
        ),
    ]
