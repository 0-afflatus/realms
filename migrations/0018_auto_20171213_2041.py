# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realms', '0017_auto_20171213_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='page_slug',
            field=models.CharField(verbose_name='URL slug', max_length=255, blank=True, help_text='URL friendly name; lowercase, numbers and underscores only.'),
        ),
    ]
