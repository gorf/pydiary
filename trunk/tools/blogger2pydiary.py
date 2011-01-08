#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""模块名
@version: $Id$
@author: U{Liu Qing}
"""
__author__ =  '刘清'
__version__=  '1.0'
__nonsense__ = ''

from blogger import *
import psycopg2, codecs

source = 'blog-11-23-2009.xml'
blogger = Blogger(open(source))
target = [i for i in blogger.posts()]
conn = psycopg2.connect("dbname = 'pylogs' host = 'localhost' user = 'lq' password = 'luukher'")
cur = conn.cursor()
for i in range(len(target)):
    print target[i]['title']
    target[i]['title']=target[i]['title'].encode("utf-8")
    target[i]['content']=target[i]['content'].encode("utf-8")
    target[i]['id']=target[i]['id'][35:]

    cur.execute("""INSERT INTO blog_post
        (title,content,post_name,post_type,post_status,pubdate,hits,menu_order,comment_status,comment_count) VALUES
        (%(title)s,%(content)s,%(id)s,'post','publish',%(published)s,500,0,'open',0);""",target[i])
    #posts = cur.fetchall()
conn.commit()
cur.close()
conn.close()

