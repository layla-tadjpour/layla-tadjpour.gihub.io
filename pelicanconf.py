#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Layla Tadjpour'
SITENAME = u"Layla Tadjpour"
SITEURL = u"https://layla-tadjpour.github.io"
SITESUBURL = '/'
SITETITLE = AUTHOR
SITESUBTITLE = u''
SITEDESCRIPTION = u'%s\'s Thoughts and Writings' % AUTHOR
SITELOGO = u'../images/profile.png'
BROWSER_COLOR = '#333'
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

#USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
#HOME_HIDE_TAGS = True

# Blogroll
#LINKS = (
#         ('fast.ai',"http://www.fast.ai/"),
#        )


# Feeds 
FEEDS =  (('All posts', 'feeds/all.atom.xml'),
          ('Category', 'feeds/category'),
          )


# Social widget
SOCIAL = (
         ('github', 'https://github.com/layla-tadjpour'),
         ('twitter', 'https://twitter.com/laylatadjpour'),
         ('linkedin', 'https://www.linkedin.com/in/layla-tadjpour-6144602/'),
         )

MENUITEMS = (  
             ('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),  
             )


COPYRIGHT_NAME =  'Layla Tadjpour'

COPYRIGHT_YEAR =  2018

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False
DISPLAY_PAGES_ON_MENU = True
STATIC_PATHS = ['images',]
MY_EMAIL_ADDR = 'layla.tadjpour@gmail.com'
#TWITTER_USERNAME = '@laylatadjpour'
PAGE_URL = f"{SITEURL}"
#PAGE_SAVE_AS = f"{SITEURL}/index.html"
