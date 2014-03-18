"""
	This is the testing suite for the web frontent to TwitterPoemBot

	To run this server, just type in the following command:
		python tpgserver_test.py
"""
import os
import tpgserver
import unittest


class TpgTester(unittest.TestCase):
	"""This class contains tests for the flask frontend"""

	def setUp(self):
		self.app = tpgserver.app.test_client()
	def tearDown(self):
		pass

	def test_home_page(self):
		"""test to make sure the home page has some elements"""
		rv = self.app.get("/")
		assert "Twitter Poem Generator" in rv.data
		# the following urls shouldn't appear on the debug page
		assert "bootstrapcdn.com" in rv.data
		assert "ajax.googleapis.com" in rv.data
	def test_query(self):
		"""check to make sure queries can be sent and stored"""
		rv = self.app.post("/generate",
				data = {"query": "antimage"},
				follow_redirects=True)
		assert "antimage" in rv.data
	def test_invalid_poem_url(self):
		"""check tomake sure completely invalid id values don't work"""
		rv = self.app.get("/poem/asdf")
		assert "invalid url" in rv.data

	def test_invalid_poem_id(self):
		"""check to make sure invalid poem ids don't work"""
		rv = self.app.get("/poem/{0}".format(len(tpgserver.queries)))
		assert "query not found" in rv.data

if __name__ == "__main__":
	unittest.main()
