# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realms', '0010_auto_20171201_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realm',
            name='magic_level',
            field=models.IntegerField(default=0, choices=[(0, 'Historical'), (1, 'Folkloric'), (2, 'Miraculous'), (3, 'Low magic'), (4, 'Heroic'), (5, 'Mythical'), (6, 'Paranormal'), (7, 'Enchanted'), (8, 'High magic'), (9, 'Very High magic')], help_text='Magical fantasy level'),
        ),
        migrations.AlterField(
            model_name='realm',
            name='tech_level',
            field=models.IntegerField(default=0, choices=[(0, 'Stone Age'), (1, 'Bronze Age'), (2, 'Iron Age'), (3, 'Medieval'), (4, 'Colonial Age'), (5, 'Industrial Age'), (6, 'Steam Age'), (7, 'Nuclear Age'), (8, 'Digital Age'), (9, 'Microtech Age')], help_text='Technological level'),
        ),
    ]
