# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realms', '0006_realm_banner'),
    ]

    operations = [
        migrations.AddField(
            model_name='realm',
            name='meta_map',
            field=models.ImageField(blank=True, help_text='600*800 pixel map of your world.', upload_to=''),
        ),
        migrations.AddField(
            model_name='realm',
            name='wallpaper',
            field=models.ImageField(blank=True, help_text='768*1024 pixel background image.', upload_to=''),
        ),
    ]
