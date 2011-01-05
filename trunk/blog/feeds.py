#!/usr/bin/env python
#coding=utf-8
from django.utils.translation import ugettext as _
from django.core.exceptions import ObjectDoesNotExist
from django.utils.feedgenerator import Atom1Feed
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.contrib.syndication.feeds import Feed
from models import Post,Category
from utils import html
from blog import models
current_site = Site.objects.get_current().name

global_title_template = 'blog/feeds/title.html'
global_description_template = 'blog/feeds/description.html'
global_item_copyright = 'Pylogs by Sky'
global_title = _("Pylogs: Latest Posts")
global_description = _("logging your life...")
class RssLatestPosts(Feed):
    """
    RSS Feed of the most recently published posts.    
    """    
    title_template = global_title_template
    description_template = global_description_template
    item_copyright = global_item_copyright
    title = global_title
    link = "/"
    description = global_description
    author = "Pylogs RSS generator"
    
    def item_author_name(self, item):
        return 'Sky' #item.author.username
    
    def items(self):
        posts = Post.objects.filter(post_type__iexact='post',
                                    post_status__iexact = models.POST_STATUS[0][0])[:15]
        for post in posts:
            post.content = html.htmlDecode(post.content)
        return posts
    
    def item_author_name(self, item):
        return 'Sky' #item.author.username
    
    def item_link(self, item):
        return item.get_absolute_url() 
    
    def item_pubdate(self, item):
        return item.pubdate
    
class AtomLatestPosts(Feed):
    """
    Atom Feed of the most recently published posts.    
    """
    feed_type = Atom1Feed
    title_template = global_title_template
    description_template = global_description_template
    item_copyright = global_item_copyright
    title = global_title
    link = "/"
    subtitle = global_description
    author = "Pylogs ATOM generator"
    
    def item_author_name(self, item):
        return 'Sky' #item.author.username
    
    def items(self):
        posts = Post.objects.filter(post_type__iexact='post',
                                    post_status__iexact = models.POST_STATUS[0][0])[:15]
        for post in posts:
            post.content = html.htmlDecode(post.content)
        return posts
    
    def item_author_name(self, item):
        return 'Sky' #item.author.username
    
    def item_link(self, item):
        return item.get_absolute_url() 
    
    def item_pubdate(self, item):
        return item.pubdate