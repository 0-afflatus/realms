# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realms', '0022_auto_20171214_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realm',
            name='banner',
            field=models.ImageField(blank=True, help_text='250 * 1000 pixel banner image.', upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='realm',
            name='meta_map',
            field=models.ImageField(blank=True, help_text='600 * 800 pixel map of your world.', upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='realm',
            name='wallpaper',
            field=models.ImageField(blank=True, help_text='768 * 1024 pixel background image.', upload_to='uploads/'),
        ),
    ]
