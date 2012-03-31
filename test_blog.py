import unittest
import json
import os
from simpleBlog import Entries
from simpleBlog import *

class BlogTests(unittest.TestCase):
	@classmethod
	def setUpClass(self):
		pass
		
	def test_should_be_able_to_flatten_an_array(self):
		entry_stencil = read("templates/entry.template")
		# This is not only the shortest but apparently also pretty fast: http://www.skymind.com/~ocrow/python_string/
		templates = [template(entry_stencil, entry) for entry in Entries()]
		markup = ''.join(templates) 
		# print markup
		
	@classmethod
	def tearDownClass(self):
		pass
		

def read_json_object(path):
	return load(open(path, 'r'))
		
if __name__ == '__main__':
	unittest.main()
