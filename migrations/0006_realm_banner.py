# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realms', '0005_auto_20171130_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='realm',
            name='banner',
            field=models.ImageField(blank=True, help_text='250*1000 pixel banner image.', upload_to=''),
        ),
    ]
