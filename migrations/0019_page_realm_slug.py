# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realms', '0018_auto_20171213_2041'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='realm_slug',
            field=models.CharField(verbose_name='Realm URL slug', max_length=255, default='glysa', help_text='URL friendly name; lowercase, numbers and underscores only.'),
            preserve_default=False,
        ),
    ]
