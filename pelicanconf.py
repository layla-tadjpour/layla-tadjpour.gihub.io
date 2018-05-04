#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Layla Tadjpour'
SITENAME = 'Layla Tadjpour'
SITEURL = ''
THEME = 'Flex'
PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
         ("Layla Tadjpour", "https://layla-tadjpour.github.io"),
        )
#LINKS = (('github', 'https://github.com/layla-tadjpour'),
#        ('twitter', 'https://twitter.com/laylatadjpour'),
#        ('linkedin', 'https://www.linkedin.com/in/layla-tadjpour-6144602/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

SOCIAL = (
         ('github', 'https://github.com/layla-tadjpour'),
         ('twitter', 'https://twitter.com/laylatadjpour'),
         ('linkedin', 'https://www.linkedin.com/in/layla-tadjpour-6144602/'),
         )


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
DISPLAY_PAGES_ON_MENU = True