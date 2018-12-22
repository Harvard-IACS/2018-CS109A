SITE_NAME = '2018-CS109A'

COURSE_NAME = 'CS109A: Introduction to  Data Science'

AUTHOR = 'Pavlos Protopapas, Kevin Rader'

SITEURL = 'https://harvard-iacs.github.io/2018-CS109A'

GITHUB = 'https://github.com/Harvard-IACS/2018-CS109A'

COLOR = '#A51C30'

MENUITEMS = [
    ('Syllabus', 'pages/syllabus.html'),
    ('Schedule', 'pages/schedule.html'),
    ('Materials', 'pages/materials.html')
]


NAVBAR_LINKS = []

PATH = 'content'

OUTPUT_PATH = 'docs'

TIMEZONE = 'EST'

DEFAULT_LANG = 'en'

FEED_ALL_ATOM = None

CATEGORY_FEED_ATOM = None

TRANSLATION_FEED_ATOM = None

AUTHOR_FEED_ATOM = None

AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

DEFAULT_CATEGORY = 'pages'

AUTHORS_SAVE_AS = ''

CATEGORIES_SAVE_AS = ''

ARCHIVES_SAVE_AS = ''

TAGS_SAVE_AS = ''

ARTICLE_SAVE_AS = '{category}/{slug}.html'

AUTHOR_URL = ''

THEME_STATIC_DIR = 'style'

DELETE_OUTPUT_DIRECTORY = True

MARKUP = ['md', 'ipynb']

PLUGIN_PATHS = ['./plugins']

PLUGINS = ['ipynb.markup', 'dateish']

IGNORE_FILES = ['.ipynb_checkpoints']

DATEISH_PROPERTIES = ['due']

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

import re

JINJA_FILTERS = {
    'original_content': lambda x: re.search(r"content/.*", x).group(0)
}

USE_FOLDER_AS_CATEGORY = False

IGNORE_FILES = ['README.md']
