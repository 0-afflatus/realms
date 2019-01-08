# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realms', '0019_page_realm_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realm',
            name='wallpaper',
            field=models.ImageField(blank=True, default='/static/images/dungeondisorder.jpg', help_text='768 * 1024 pixel background image.', upload_to='uploads'),
        ),
    ]
