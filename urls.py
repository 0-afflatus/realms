#! /usr/bin/env python3
# -*- coding: UTF8 -*-

"""Realms - urls.py

RPG Campaign Organiser
"""

__version__ = 0.1
__maintainer__ = "afflatus@maginaria.com"

# Modules

# realms/urls.py
from django.conf.urls import url
from realms import views

urlpatterns = [
	url(r'^$', views.realm_new, name='realm_new'),
	url(r'^(?P<realm_slug>\w+)/$', views.realm_view, name='realm_view'),
	url(r'^(?P<realm_slug>\w+)/edit/$', views.realm_edit, name='realm_edit'),
    url(r'^(?P<realm_slug>\w+)/del/$', views.realm_delete, name='realm_delete'),
    url(r'^(?P<realm_slug>\w+)/new_page/$', views.page_new, name='page_new'),
    url(r'^(?P<realm_slug>\w+)/(?P<page_slug>\w+)/$', views.page_view, name='page_view'),
    url(r'^(?P<realm_slug>\w+)/(?P<page_slug>\w+)/edit/$', views.page_edit, name='page_edit'),
    url(r'^(?P<realm_slug>\w+)/(?P<page_slug>\w+)/del/$', views.page_delete, name='page_delete'),
]

handler403 = views.handler403
handler404 = views.handler404
handler500 = views.handler500
