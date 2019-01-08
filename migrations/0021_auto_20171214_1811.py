# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realms', '0020_auto_20171214_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realm',
            name='wallpaper',
            field=models.ImageField(blank=True, default='./dungeondisorder.jpg', help_text='768 * 1024 pixel background image.', upload_to='uploads'),
        ),
    ]
