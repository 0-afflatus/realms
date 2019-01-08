# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realms', '0004_auto_20171130_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='realm',
            name='magic_level',
            field=models.IntegerField(default=0, help_text='0: No magic - 9: High Magic.'),
        ),
        migrations.AddField(
            model_name='realm',
            name='tech_level',
            field=models.IntegerField(default=0, help_text='0: Stone Age, 1: Bronze Age, 2: Iron Age, 3: Medieval, 4: Colonial Age, 5: Industrial Age, 6: Steam Age, 7: Nuclear Age, 8: Digital Age, 9: Microtech Age.'),
        ),
    ]
