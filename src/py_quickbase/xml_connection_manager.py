from py_quickbase import Plumbing

class XMLQuickBaseConnection(Plumbing.ConnectionManager):
    
    # ======================================================
    # Quickbase API Methods
    # ======================================================
    
    def authenticate(self, username, password):
        """You must log in before you make a call to QuickBase"""
        url = self._base_url(False) + "db/main"
        xml = XMLBuilder(format=True)
        with xml.qdbapi():
            with xml.sub_tag("username"):
                xml << username
            with xml.sub_tag("password"):
                xml << password
            
        
    
    