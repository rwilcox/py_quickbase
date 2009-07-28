""" Gives both a test to make sure we're using wsgi_intercept correctly, and shows us how it's done..."""

from __future__ import with_statement

import unittest
from wsgi_intercept.urllib2_intercept import install_opener
install_opener()    # Does the replacing...
#import urllib2

import wsgi_intercept

from test_helpers import *

def ourResponseFunction(environ, start_response):
	status = '200 OK'
	response_headers = [('Content-type','text/plain')]
	start_response(status, response_headers)
	return ['Hello world!!\n']

class postTestAndResponseObject(object):
	def __init__(self):
		self.postedInfo = ""
	
	def __call__(self, environ, start_response):
		self.postedInfo = environ['wsgi.input'].read()
		#print start_response
		#print start_response.__class__
		#print start_response.read()
		
		status = '200 OK'
		response_headers = [('Content-type','text/plain')]
		start_response(status, response_headers)
		return ['Hello world!!\n']
		
	


class TestWSGIIntercept(unittest.TestCase):
	def test_simple_request(self):
		
		def create_fn():
			return ourResponseFunction
		
		with fakeConnection('www.example.com', 80, create_fn, "/"):
			import urllib2
			self.assertEquals("Hello world!!\n", urllib2.urlopen("http://www.example.com:80/").read()) 
	
	def test_file_on_path(self):
		def create_fn():
			return ourResponseFunction
		
		with fakeConnection('www.example.com', 80, create_fn, '/some_page.html'):
			import urllib2
			self.assertEquals("Hello world!!\n", urllib2.urlopen("http://www.example.com:80/some_page.html").read()) 

	def test_post_request(self):
		self.ourPostAndResponseObject = None
		def create_fn():
			self.ourPostAndResponseObject = postTestAndResponseObject()
			return self.ourPostAndResponseObject
		
		expectedData = 'This data is passed to stdin of the CGI'
		with fakeConnection('www.example.com', 80, create_fn, '/some_post_page.html'):
			import urllib2
			req = urllib2.Request(url='https://www.example.com/some_post_page.html', data=expectedData)
			f = urllib2.urlopen(req) 
		self.assertEquals( self.ourPostAndResponseObject.postedInfo, expectedData)
	
if __name__ == '__main__':
	unittest.main()
