#!/usr/bin/env python
#coding=utf-8
from django.template import Library
from django.conf import settings

from utils.version import get_svn_revision
from blog.models import Setting

register = Library()
VERSION = getattr(settings,'VERSION','unknown')
def get_version():
    """
    Returns the version as a human-format string.
    """
    v = '.'.join([str(i) for i in VERSION[:-1]])
    if VERSION[-1]: 	   
        v = '%s%s %s' % (v, VERSION[-1],get_svn_revision())
    return v

    

def site_name():
    '''site name'''
    return get_setting_section('SiteName')
 	
def site_subtitle():
    return get_setting_section('SiteSubTitle')

register.simple_tag(get_version)
register.simple_tag(site_name)
register.simple_tag(site_subtitle)
 	
def get_setting_section(section):
    setting_object = Setting.objects.filter(setting_name__exact=section)
    if setting_object:
        return setting_object[0].setting_value
    else:
        return ''
