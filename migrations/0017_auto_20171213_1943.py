# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realms', '0016_page'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='slug',
            new_name='page_slug',
        ),
        migrations.RenameField(
            model_name='realm',
            old_name='slug',
            new_name='realm_slug',
        ),
    ]
