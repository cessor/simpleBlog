import unittest
import json
import os
import entries
from simpleblog import *

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
		
	def test_replace_twitter_names(self):
		text = "@cessor" 
		text = filter(text)
		self.assertEqual(text, "<a href='https://twitter.com/cessor'>@cessor</a>")
		
	@classmethod
	def tearDownClass(self):
		pass

def read_json_object(path):
	return load(open(path, 'r'))
		
if __name__ == '__main__':
	unittest.main()
