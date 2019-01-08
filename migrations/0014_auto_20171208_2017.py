# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('realms', '0013_auto_20171203_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realm',
            name='banner',
            field=models.ImageField(blank=True, help_text='250 * 1000 pixel banner image.', upload_to='uploads'),
        ),
        migrations.AlterField(
            model_name='realm',
            name='description',
            field=markdownx.models.MarkdownxField(blank=True, default='Describe your Realm here ...', help_text='General description; use markdown for formatting.'),
        ),
        migrations.AlterField(
            model_name='realm',
            name='meta_map',
            field=models.ImageField(blank=True, help_text='600 * 800 pixel map of your world.', upload_to='uploads'),
        ),
        migrations.AlterField(
            model_name='realm',
            name='name',
            field=models.CharField(max_length=255, default='My Cool Realm', help_text='Name of your realm; universe, milieu or game setting.'),
        ),
        migrations.AlterField(
            model_name='realm',
            name='slug',
            field=models.CharField(max_length=255, help_text='URL friendly name; lowercase, numbers and underscores only.'),
        ),
        migrations.AlterField(
            model_name='realm',
            name='wallpaper',
            field=models.ImageField(blank=True, help_text='768 * 1024 pixel background image.', upload_to='uploads'),
        ),
    ]
