import unittest
import requests

from flask import Flask
from flask_testing import TestCase

class SampleTest(unittest.TestCase):

	BASE_URL = "http://192.168.0.188:5000"

	BOOKS_URL = "{}/books".format(BASE_URL)

	# test case to check app creation using configured items
	def create_app(self):
		app = Flask(__name__)
		app.config['TESTING'] = True
		app.config['LIVESERVER_PORT'] = 5000
		app.config['LIVESERVER_TIMEOUT'] = 10
		return app

	# test case to check if get response is successful with given json payload
	def test_GetBooks(self):
		r = requests.get(self.BOOKS_URL, json={"rows":3})
		# data = len(r.json()["books"])
		self.assertEqual(r.status_code, 200)
		self.assertEqual(len(r.json()["books"]), 3)
		self.assertNotEqual(len(r.json()["books"]), 5)

	# test case to for failure checking
	def test_Failure(self):
		r = requests.get(self.BOOKS_URL, json={"rows":2})
		# data = len(r.json()["books"])
		self.assertEqual(r.status_code, 200)
		self.assertEqual(len(r.json()["books"]), 3)


	def test_GetFilteredBooks(self):
		r = requests.get(self.BOOKS_URL, json={"title":"Friction, Volume 7: Best Gay Erotic Fiction"})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(len(r.json()["books"]), 1)	

	def test_BADRequest(self):
		r = requests.get(self.BOOKS_URL, json={"title":"Some Random Title"})
		# if r.json()["books"]==None:
			# print("No books found with this criteria")
		self.assertEqual(r.status_code, 200)
		self.assertIsNone(r.json()["books"],"No Books are available.")	

	def test_BADRequest_2(self):
		r = requests.get(self.BOOKS_URL, json={"Random ColumnName":"Some Random Title"})
		# if r.json()["message"]==None:
			# print("No books found with this criteria")
		self.assertEqual(r.status_code, 404)
		print(r.json()["message"])


if __name__ == '__main__':
    unittest.main()
