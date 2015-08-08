#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = 'Ziaa'
SITENAME = 'Pelican Persian blog starting point'
SITEURL = ''

PATH = 'content'
SCRIPT_PATH = os.path.realpath(__file__)
BLOG_BASE_PATH = os.path.dirname(SCRIPT_PATH)

TIMEZONE = 'Asia/Tehran'

DEFAULT_LANG = 'fa'
DATE_FORMATS = {
    'fa': '%A %d %B %Y'
}
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Set the theme
THEMES_PATH = os.path.join(BLOG_BASE_PATH, 'themes/')
THEME = os.path.join(THEMES_PATH, 'Pelican-RTL-theme/')

# Plugins
PLUGIN_PATHS = ["plugins"]
PLUGINS = ["pelican_persian_date"]
