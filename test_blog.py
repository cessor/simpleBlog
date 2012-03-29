import unittest
import json
import os
from make_blog_entry import *

class BlogTests(unittest.TestCase):
	@classmethod
	def setUpClass(self):
		self.test_file_path = 'test.json'
		with open(self.test_file_path,'w') as f:
			f.write('{ "test" : "this is a test"}')

	def test_json_can_read_a_file_directly(self):
	    object = read_json_object(self.test_file_path)
	    self.assertEqual(object["test"], "this is a test")

	@classmethod
	def tearDownClass(self):
		os.remove(self.test_file_path)

if __name__ == '__main__':
	unittest.main()
