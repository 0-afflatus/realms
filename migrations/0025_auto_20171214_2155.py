# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realms', '0024_auto_20171214_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='realm_slug',
            field=models.CharField(verbose_name='Realm URL slug', max_length=255, blank=True, help_text='URL friendly name; lowercase, numbers and underscores only.'),
        ),
    ]
