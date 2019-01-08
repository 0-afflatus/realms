#! /usr/bin/env python3
# -*- coding: UTF8 -*-

"""Realms - models.py

RPG Campaign Organiser
"""

__version__ = 0.1
__maintainer__ = "afflatus@maginaria.com"

# Modules

from django.db import models
from django.utils import timezone
from markdownx.models import MarkdownxField

class Realm(models.Model):
    tech_levels = [
        (1, 'Stone Age'), 
        (2, 'Bronze Age'), 
        (3, 'Iron Age'), 
        (4, 'Medieval'), 
        (5, 'Colonial Age'), 
        (6, 'Industrial Age'), 
        (7, 'Steam Age'), 
        (8, 'Nuclear Age'), 
        (9, 'Digital Age'), 
        (10, 'Microtech Age') 
    ]
    magic_levels = [
        (1, 'Historical'), 
        (2, 'Folkloric'), 
        (3, 'Miraculous'), 
        (4, 'Low magic'), 
        (5, 'Heroic'), 
        (6, 'Mythical'), 
        (7, 'Paranormal'), 
        (8, 'Enchanted'), 
        (9, 'High magic'), 
        (10, 'Very High magic')
    ]
    
    name = models.CharField (
        max_length=255, 
        verbose_name="Realm Name", 
        default='My Cool Realm', 
        help_text='Name of your realm; universe, milieu or game setting.'
    )
    author = models.ForeignKey ('auth.User')
    created_date = models.DateTimeField(default=timezone.now)
    
    realm_slug = models.CharField (
        max_length=255, 
        verbose_name="URL slug", 
        help_text = 'URL friendly name; lowercase, numbers and underscores only.'
    )
    description = MarkdownxField (
        blank = True, 
        default = 'Describe your Realm here ...', 
        help_text = 'General description; use markdown for formatting.'
    )
    brief_text = models.CharField (
        max_length=225,
        blank = True, 
        help_text = "Brief paragraph overview of the game."
    )
    rule_set = models.CharField (
        max_length=127, 
        blank = True, 
        help_text = "D&amp;D, GURPS or your own custom rules."
    )
    genre = models.CharField(
        max_length=127, 
        blank = True, 
        help_text = "Genre"
    )
    tech_level = models.IntegerField (
        default = 1, 
        choices = tech_levels, 
        help_text = "Technological level"
    )
    magic_level = models.IntegerField (
        default = 1, 
        choices = magic_levels, 
        help_text = "Magical fantasy level"
    )
    brief_img = models.ImageField (
        upload_to = 'uploads/', 
        blank = True, 
        help_text = "600 * 800 pixel map or landscape of your world."
    )
    wallpaper = models.ImageField (
        upload_to = 'uploads/', 
        blank = True, 
        help_text = "768 * 1024 pixel background image."
    )
    
    def __str__(self):
        return self.name

class Page(models.Model):
    title = models.CharField (
        max_length = 255, 
        verbose_name = "Page Title", 
        default = '', 
        help_text = 'Page Title'
    )
    author = models.ForeignKey ('auth.User')
    created_date = models.DateTimeField (default = timezone.now)
    # change to slug field
    page_slug = models.CharField (
        blank = True, 
        max_length = 255, 
        verbose_name = "URL slug", 
        help_text = 'URL friendly name; lowercase, numbers and underscores only.'
    )
    realm_slug = models.CharField(
        blank = True, 
        max_length=255, 
        verbose_name="Realm URL slug", 
        help_text = 'URL friendly name; lowercase, numbers and underscores only.'
    )
    description = MarkdownxField (
        blank = True, 
        default = 'Body Text', 
        help_text = 'Use markdown for formatting.'
    )
    
