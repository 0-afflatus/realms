# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realm',
            name='name',
            field=models.CharField(max_length=255, default='My Cool Realm', help_text='Your universe, milieu or game setting.'),
        ),
    ]
