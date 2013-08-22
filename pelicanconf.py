#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'LucasWei'
SITENAME = u"Lucas's 部落格"
SITESUBTITLE = u"Lucas's blogging space"
SITEURL = ''

TIMEZONE = 'Asia/Taipei'

DEFAULT_LANG = u'zh-TW'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

#Github
GITHUB_URL = 'https://github.com/lucaswei/lucaswei.github.io'

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          )

# Social widget
SOCIAL = (('Plurk', 'http://www.plurk.com/lucas0412'),
          ('Github', 'https://github.com/lucaswei'),)

# copy images in content directory in to output space 
STATIC_PATHS = ['images',]

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
THEME = "./theme/gum/"
