#-*- coding:utf-8 -*-
from os import path
#from django.utils.translation import ugettext as _

DEBUG = True
#DEBUG = True 
ALLOWED_HOSTS = ['gentoogle.com', 'www.gentoogle.com', '139.162.81.219']
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'pylogs',                      # Or path to database file if using sqlite3.
        'USER': 'blog',                      # Not used with sqlite3.
        'PASSWORD': 'luukher',                  # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

TIME_ZONE = 'Asia/Chongqing'
LANGUAGE_CODE = 'zh-cn'
SITE_ID = 1

USE_I18N = True
FORCE_SCRIPT_NAME = ''

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = path.join(path.dirname(__file__),'../media')
#print MEDIA_ROOT
ALLOW_FILE_TYPES = ('.jpg','.gif','.png')
# URL that handles the media served from MEDIA_URL.
#MEDIA_URL = '/pylogs/media'
MEDIA_URL = '/media/'
# the theme name 'default, techicon, beijing2008'
THEME_NAME = 'techicon'
#THEME_NAME = 'default'
#THEME_NAME = 'beijing2008'

#STATIC_PATH = '/var/www/localhost/htdocs/pylogs/media'
STATIC_PATH = './media'

# Django 1.4+ 已弃用，admin 静态文件改用 STATIC_URL
# ADMIN_MEDIA_PREFIX = '/admin_media/'

# 静态文件收集目录（执行 collectstatic 后，admin 的 CSS/JS/图标会放这里）
STATIC_ROOT = path.join(path.dirname(__file__), '../static')

#Send Email settings
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'qingyuan.liu@gmail.com'
EMAIL_HOST_PASSWORD = '2basic2'
EMAIL_USE_TLS = True

SECRET_KEY = 'zb2&a4g41snkt&*c92s=djl+*fcp((i85w(k&&)#$5j!+zz!!*'
#setting session expire after half a hour.
#SESSION_COOKIE_AGE =  60 * 30

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
)
INTERNAL_IPS = ('127.0.0.1',)

ROOT_URLCONF = 'pydiary.urls'
#print path.join(path.dirname(__file__)
TEMPLATE_DIRS = (path.join(path.dirname(__file__),'../templates'),)
#print TEMPLATE_DIRS 
#TEMPLATE_DIRS = ( os.path.join(SITE_ROOT, 'templates'),)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    #'debug_toolbar',
    'blog',
    'todo',
    'filemanager',
    'wap',    
    #'tests',
)
VERSION = (1, 15, 'beta')	
STATIC_URL = '/static/'
 
 
#FEED CONF START
FEED_BLOG_URL_PREFIX = "http://gentoogle.com/"  #change to your site url
FEED_POST_AUTHOR_NAME = "Gorf"
FEED_COPYRIGHT =  "Gorf的日复一日emerge"
FEED_GLOBAL_TITLE = "Gorf 的日复一日Emerge: 最新文章"
FEED_GLOBAL_DESCRIPTION = "记录你的生活……"
#FEED CONF END
