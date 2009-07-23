""" Gives both a test to make sure we're using wsgi_intercept correctly, and shows us how it's done..."""

import unittest
from wsgi_intercept.urllib2_intercept import install_opener
install_opener()    # Does the replacing...


import wsgi_intercept

def ourResponseFunction(environ, start_response):
	status = '200 OK'
	response_headers = [('Content-type','text/plain')]
	start_response(status, response_headers)
	return ['Hello world!!\n']

class TestWSGIIntercept(unittest.TestCase):
	def test_simple_request(self):
		
		def create_fn():
			return ourResponseFunction
		
		wsgi_intercept.add_wsgi_intercept('www.example.com/', 80, create_fn)
		import urllib2
		self.assertEquals("Hello world!!\n", urllib2.urlopen("http://www.example.com:80/").read()) 
	
	def test_file_on_path(self):
		def create_fn():
			return ourResponseFunction
		
		wsgi_intercept.add_wsgi_intercept('www.example.com', 80, create_fn, '/some_page.html')
		import urllib2
		self.assertEquals("Hello world!!\n", urllib2.urlopen("http://www.example.com:80/some_page.html").read()) 

if __name__ == '__main__':
	unittest.main()
