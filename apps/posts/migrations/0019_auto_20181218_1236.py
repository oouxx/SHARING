# Generated by Django 2.0 on 2018-12-18 12:36

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0018_auto_20181218_0915'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=20, verbose_name='标题')),
                ('release_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='发布时间')),
                ('modify_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='最新修改时间')),
                ('description', mdeditor.fields.MDTextField(verbose_name='详情')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='提出问题者')),
            ],
            options={
                'verbose_name': '问答',
                'verbose_name_plural': '问答',
            },
        ),
        migrations.AlterField(
            model_name='experience',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='experience', to=settings.AUTH_USER_MODEL, verbose_name='经验分享者'),
        ),
    ]
