# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realms', '0012_auto_20171203_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realm',
            name='magic_level',
            field=models.IntegerField(default=1, choices=[(1, 'Historical'), (2, 'Folkloric'), (3, 'Miraculous'), (4, 'Low magic'), (5, 'Heroic'), (6, 'Mythical'), (7, 'Paranormal'), (8, 'Enchanted'), (9, 'High magic'), (10, 'Very High magic')], help_text='Magical fantasy level'),
        ),
        migrations.AlterField(
            model_name='realm',
            name='tech_level',
            field=models.IntegerField(default=1, choices=[(1, 'Stone Age'), (2, 'Bronze Age'), (3, 'Iron Age'), (4, 'Medieval'), (5, 'Colonial Age'), (6, 'Industrial Age'), (7, 'Steam Age'), (8, 'Nuclear Age'), (9, 'Digital Age'), (10, 'Microtech Age')], help_text='Technological level'),
        ),
    ]
