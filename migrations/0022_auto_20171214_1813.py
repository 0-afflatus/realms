# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realms', '0021_auto_20171214_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realm',
            name='wallpaper',
            field=models.ImageField(blank=True, help_text='768 * 1024 pixel background image.', upload_to='uploads'),
        ),
    ]
