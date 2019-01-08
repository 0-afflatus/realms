# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realms', '0002_auto_20171130_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='realm',
            name='description',
            field=models.TextField(blank=True, default='Describe your Realm here ...', help_text='General description.'),
        ),
    ]
