import unittest
from selenium import webdriver
from test import login, home

# so what's going on here? well, we're using unittest as our test management software
# and selenium as our framework for controlling the software 
# I've factored out the page interface stuff into home.py and login.py
# this factoring-out is good because it creates a layer of tooling between the product
# and the actual test specification which we'll be putting in this document

class MainPageSmokeTests(unittest.TestCase):

	def setUp(self):
		"""
		Setup function before each test
		webdriver with chrome, we're just going to feed it the url manually since this is for the page
		"""
		self.driver = webdriver.Chrome()
		self.driver.get("file:///C:/Users/Noah/workspace/ableto/app/login.html")

	def test_add_employee_with_deduction(self):
		"""
		Test Case 1 - Employee with no deduction
		Login, and add an employee with no deduction
		"""
		loginpage = login.LoginPage(self.driver)
		self.assertTrue(loginpage.is_title_matches())
		# instantiate page object, check that we have the right title
		loginpage.adminlogin()
		# log in 
		homepage = home.HomePage(self.driver)
		# we're now on a new page, so we instantiate a home page obj, check title
		self.assertTrue(homepage.is_title_matches())
		homepage.add_new_employee_1()
		self.assertTrue(homepage.is_employee_1_matches())
		# add "employee 1" and check it matches.
		# in an ideal circumstance i'd probably have a few employe adds and checks
		# we would want to give them more distinct names in that case, but this is fine for an example

	def tearDown(self):
		"""
		tearDown function after each test
		close the driver
		"""
		self.driver.close()

if __name__ == "__main__":
    unittest.main()