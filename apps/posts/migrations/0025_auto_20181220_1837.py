# Generated by Django 2.0 on 2018-12-20 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0024_auto_20181220_1232'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experience',
            name='icon',
        ),
        migrations.AddField(
            model_name='opensource',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='media/opensource/cover/%Y/%m', verbose_name='封面'),
        ),
        migrations.AddField(
            model_name='programming',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='media/programming/cover/%Y/%m', verbose_name='封面'),
        ),
        migrations.AlterField(
            model_name='software',
            name='icon',
            field=models.ImageField(blank=True, default='/media/default_avatar.jpeg', null=True, upload_to='media/software/icon/%Y/%m', verbose_name='软件icon'),
        ),
    ]