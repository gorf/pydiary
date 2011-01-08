#!/usr/bin/env python
# encoding: utf-8

"""A Blogger export data to Python data tool"""

__version__ = "0.1"

import re
import datetime
from xml.dom import minidom
from xml.parsers.expat import ExpatError, ErrorString

class XmlError(Exception):
    pass


class Blogger(object):
    """A class to parse Blogger export XML"""
    def __init__(self, xml):
        """takes either a string or a file-like object

        Usage:
        >>> blogger = Blogger(open('path/to.xml'))
        >>> blogger = Blogger('<xml></xml>')
        """
        if hasattr(xml, 'read'):
            """file-like object"""
            xml = xml.read()
        try:
            self.xml = minidom.parseString(xml)
        except ExpatError, error:
            raise XmlError, ErrorString(error.code)
        except TypeError, error:
            # probably wasn't XML
            raise XmlError, error

    def posts(self, with_comments=None):
        """returns a list of posts in random order

        Usage:
        >>> blogger = Blogger(open('path/to.xml'))
        >>> [i for i in blogger.posts()]
        [{
            'id':'tag:blogger.com,1999:blog-7219822.post-111599600799349916',
            'published': (2009, 1, 1, 13, 45, 34),
            'updated': (2009, 1, 1, 13, 45, 34),
            'title': "My blog post",
            'content':'<p>Something</p>'
        }]
        """
        entries = self.xml.getElementsByTagName('entry')
        for entry in entries:
            if (entry.getElementsByTagName('category')[0].getAttribute('term') ==
                'http://schemas.google.com/blogger/2008/kind#post'):
                try:
                    data = {
                        'id': get_first_node_data(entry, 'id'),
                        'published': iso8601_to_datetime(get_first_node_data(entry, 'published')),
                        'updated': iso8601_to_datetime(get_first_node_data(entry, 'updated')),
                        'title': get_first_node_data(entry, 'title'),
                        'content': get_first_node_data(entry, 'content'),
                    }
                except ExpatError, error:
                    continue
                yield data


def get_first_node_data(xml_nodes, node_name):
    """Helper function to clean up parsing of XML data

    Usage:
    >>> get_first_node_data(xml.getElementsByTagName('thing'))
    u'Text'
    """
    nodes = xml_nodes.getElementsByTagName(node_name)
    try:
        data = nodes[0].firstChild.data
    except (ExpatError, AttributeError, IndexError):
        data = u""
    except Exception, error:
        raise Exception, error
    return data

def iso8601_to_datetime(iso_date):
    """Converts an ISO-8601 date string to a Python datetime.
    We ignore microseconds for the moment as datetime only takes milliseconds.

    Usage:
    >>> iso8601_to_datetime('2009-04-24T15:48:26,000000Z')
    (2009, 04, 24, 15, 48, 26)
    """
    rx = re.compile(r'^(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):(\d{2}),?(.*)$')
    matches = rx.match(iso_date)
    if matches:
        match_bits = [int(i) for i in matches.groups()[:6]]
        return datetime.datetime(*match_bits)
    return None
