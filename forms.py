#! /usr/bin/env python3
# -*- coding: UTF8 -*-

"""Realms - forms.py

RPG Campaign Organiser
"""

__version__ = 0.1
__maintainer__ = "afflatus@maginaria.com"

# Modules

from django import forms

from .models import Realm, Page

class newRealmForm(forms.ModelForm):

    class Meta:
        model = Realm
        fields = ('name',)

class RealmEditForm(forms.ModelForm):
    
    class Meta:
        model = Realm
        fields = (
            'name', 
            'realm_slug', 
            'description', 
            'brief_text',
            'rule_set', 
            'genre', 
            'tech_level', 
            'magic_level', 
            'brief_img', 
            'wallpaper',
        )

class PageEditForm(forms.ModelForm):
    
    class Meta:
        model = Page
        fields = (
            'title', 
            'realm_slug',
            'page_slug', 
            'description', 
        )
