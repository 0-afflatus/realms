# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realms', '0003_realm_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='realm',
            name='genre',
            field=models.CharField(max_length=127, blank=True, help_text='Genre'),
        ),
        migrations.AddField(
            model_name='realm',
            name='rule_set',
            field=models.CharField(max_length=127, blank=True, help_text='D&amp;D, GURPS or your own custom rules.'),
        ),
    ]
