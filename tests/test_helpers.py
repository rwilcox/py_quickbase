from __future__ import with_statement
from contextlib import contextmanager
import wsgi_intercept


@contextmanager
def fakeConnection(domain, port, call, page=None):
	"""Sets up a wsgi_intercept, calls your code inside the with statement, then removes said intercept"""
	wsgi_intercept.add_wsgi_intercept(domain, port, call, page)
	try:
		yield
		wsgi_intercept.remove_wsgi_intercept(domain, port)  # remove our intercept!
	except:
		wsgi_intercept.remove_wsgi_intercept(domain, port)  # remove our intercept!
		raise # and reraise the exception

