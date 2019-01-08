# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realms', '0007_auto_20171130_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='realm',
            name='slug',
            field=models.CharField(max_length=255, default='mycoolrealm'),
            preserve_default=False,
        ),
    ]
