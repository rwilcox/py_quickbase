from __future__ import with_statement

import xml.dom
from xmlbuilder import XMLBuilder

class ConnectionManager(object):
    """ConnectionManager takes care of the connecting to QuickBase and dealing with responses"""
    
    def __init__(self, domain, app_name, app_token = None):
        super(ConnectionManager, self).__init__()
        self.domain = domain
        self.app_token = app_token
        self.app_name = app_name
    
    def _fetch_from(self, url_after_db_id):
        """Retrieves the data from the URL. """
        pass
    
    def _handle_response(self):
        pass
    
    def _fetch_and_handle_response(self):
        """Convenience method: do the fetching and the response handling/parsing in method"""
        return self.handle_response( self.fetch() )
    
    def _base_url(self, withDBID=True):
        if withDBID:
            return "https://%(domain)s.quickbase.com/%(dbid)s" % dict(domain=self.domain, dbid=self.dbid)
        else
            return "https://%(domain)s.quickbase.com/"
    

