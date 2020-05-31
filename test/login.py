from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

uname = "admin123"
pword = "foobar123"
# generally you'd want these to be set as environmental variables
# or factored out into a variables or ini file or something, to make it easier to manage

class LoginPage(object):
	"""
	Login page action methods go here
	"""
	# so the way this kind of thing works is that we have a class whose purpose is to present functions for automatio
	# these functions can be used by any number of tests, but need maintenance and changes when the software changes
	# we save a lot of time by having one page class for each page, rather than having this stuff all over the place
	# We don't want all our page objects in one file, as if they're large (as is typical) we eventually need to split them up
	# if you split them up, probably makes sense to havem them inherit from a base page that can have __init__ and such
	def __init__(self, driver):
		self.driver = driver

	def is_title_matches(self):
		"""
		Check that login page title is correct, returns True or False
		"""
		# this kind of function is good because if you're having some kind of serious failure, this will fail first
		return "AbleTo Login Page" == self.driver.title

	def adminlogin(self):
		"""
		Log in with test credentials
		"""
		time.sleep(3) # slow because my computer is having problems! in the real world we'd have it wait for an element
		unfield = self.driver.find_element_by_name("form-username")
		unfield.send_keys(uname)
		pwfield = self.driver.find_element_by_name("form-password")
		pwfield.send_keys(pword)
		pwfield.send_keys(Keys.RETURN)
		# pretty self-explanatory. 
		# might actually be wise to factor out the element names and put a dict up top or in another file
		# from maintenance perspective