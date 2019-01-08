# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realms', '0014_auto_20171208_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realm',
            name='name',
            field=models.CharField(verbose_name='Realm Name', max_length=255, default='My Cool Realm', help_text='Name of your realm; universe, milieu or game setting.'),
        ),
        migrations.AlterField(
            model_name='realm',
            name='slug',
            field=models.CharField(verbose_name='URL slug', max_length=255, help_text='URL friendly name; lowercase, numbers and underscores only.'),
        ),
    ]
