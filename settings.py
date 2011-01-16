#-*- coding:utf-8 -*-
from os import path
DEBUG = True
TEMPLATE_DEBUG = DEBUG
#DEBUG_RPC = True

DATABASE_ENGINE = 'postgresql_psycopg2'
#DATABASE_ENGINE = 'mysql'
DATABASE_NAME = 'pylogs'
DATABASE_USER = 'root'
DATABASE_PASSWORD = ''
DATABASE_HOST = 'localhost'
DATABASE_PORT = ''

TIME_ZONE = 'Asia/Chongqing'
LANGUAGE_CODE = 'zh-cn'
SITE_ID = 1

USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = path.join(path.dirname(__file__),'media')
ALLOW_FILE_TYPES = ('.jpg','.gif','.png')
# URL that handles the media served from MEDIA_URL.
MEDIA_URL = '/media'
# the theme name 'default, techicon, beijing2008'
THEME_NAME = 'techicon'

STATIC_PATH = './media'

ADMIN_MEDIA_PREFIX = '/admin_media/'

#Send Email settings
EMAIL_HOST = 'smtp.sohu.com'
EMAIL_HOST_PASSWORD = ''
EMAIL_HOST_USER = ''

SECRET_KEY = 'zb2&a4g41snkt&*c92s=djl+*fcp((i85w(k&&)#$5j!+zz!!*'
#setting session expire after half a hour.
#SESSION_COOKIE_AGE =  60 * 30

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'urls'
TEMPLATE_DIRS = (
    path.join(path.dirname(__file__),'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'blog',
    'todo',
    'filemanager',
    'wap',    
    'tests',
    #'debug_toolbar'
)
 
 	#DEBUG_TOOLBAR_CONFIG = {'INTERCEPT_REDIRECTS': False }
 

VERSION = (1, 15, 'beta')	
 
#INTERNAL_IPS = ('127.0.0.1',)
#FEED CONF START
FEED_BLOG_URL_PREFIX = "http://code.google.com/p/pydiary/"  #change to your site url
FEED_POST_AUTHOR_NAME = "Gorf"
FEED_COPYRIGHT =  "PyDiary by Gorf"
FEED_GLOBAL_TITLE = "PyDiary: Latest Posts"
FEED_GLOBAL_DESCRIPTION = "logging your life..."
#FEED CONF END
