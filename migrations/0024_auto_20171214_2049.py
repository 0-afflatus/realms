# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realms', '0023_auto_20171214_1918'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='realm',
            name='banner',
        ),
        migrations.RemoveField(
            model_name='realm',
            name='meta_map',
        ),
        migrations.AddField(
            model_name='realm',
            name='brief_img',
            field=models.ImageField(blank=True, help_text='600 * 800 pixel map or landscape of your world.', upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='realm',
            name='brief_text',
            field=models.CharField(max_length=225, blank=True, help_text='Brief paragraph overview of the game.'),
        ),
    ]
