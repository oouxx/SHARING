# Generated by Django 2.0 on 2018-11-29 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20181129_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='software',
            name='comment_no',
            field=models.IntegerField(blank=True, null=True, verbose_name='评论数'),
        ),
        migrations.AlterField(
            model_name='software',
            name='like_no',
            field=models.IntegerField(blank=True, null=True, verbose_name='点赞数'),
        ),
    ]