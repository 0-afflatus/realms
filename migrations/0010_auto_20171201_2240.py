# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('realms', '0009_auto_20171201_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realm',
            name='description',
            field=markdownx.models.MarkdownxField(blank=True, default='Describe your Realm here ...', help_text='General description.'),
        ),
    ]
