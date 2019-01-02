import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCsase):
	"""Test for 'name_function.py"""
	
	def test_fist_last_name(self):
		"""Do name like 'Janis Joplin' work?"""
		formatted_name = get_formatted_name('janis', 'joplin')
		self.assertEqual(formatted_name, 'Janis Joplin')
	
	def test_fist_last_name(self):
		"""Do name like 'Mozart' work?"""
		formatted_name = get_formatted_name(
			'wolfgang', 'mozart', 'amadeus')
		self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')	

unitted.main()

