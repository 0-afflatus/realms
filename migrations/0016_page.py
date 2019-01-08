# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import markdownx.models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('realms', '0015_auto_20171208_2239'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='Page Title', max_length=255, default='', help_text='Page Title')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('slug', models.CharField(verbose_name='URL slug', max_length=255, help_text='URL friendly name; lowercase, numbers and underscores only.')),
                ('description', markdownx.models.MarkdownxField(blank=True, default='Body Text', help_text='Use markdown for formatting.')),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
