import cherrypy

from helpers import *


def get_cookie(key):
    """
    Returns a cookie for the key, or None if it doesn't exist
    """
    try:
        return cherrypy.request.cookie[key]
    except KeyError:
        return None


def set_cookie(key, value, path='/', expire_days=30, domain=None):
    """
    Sets a cookie's value for the specified path and expire days
    If path is None, don't set path.
    If expire_days is None, expires not set.
    """
    cherrypy.response.cookie[key] = value
    if path is not None:
        cherrypy.response.cookie[key]['path'] = path
    if expire_days is not None:
        cherrypy.response.cookie[key]['expires'] = expires_timestamp(days=expire_days)
    if domain is not None:
        cherrypy.response.cookie[key]['domain'] = domain


def clear_cookie(key, path='/', domain=None):
    """
    Clear a cookie's value
    """
    cherrypy.response.cookie[key] = ''
    if path is not None:
        cherrypy.response.cookie[key]['path'] = path
    if domain is not None:
        cherrypy.response.cookie[key]['domain'] = domain
    cherrypy.response.cookie[key]['expires'] = 0

