#! /usr/bin/env python3
# -*- coding: UTF8 -*-

"""Realms - admin.py

RPG Campaign Organiser
"""

__version__ = 0.1
__maintainer__ = "afflatus@maginaria.com"

# Modules

from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Realm, Page

admin.site.register(Realm, MarkdownxModelAdmin)
admin.site.register(Page, MarkdownxModelAdmin)
