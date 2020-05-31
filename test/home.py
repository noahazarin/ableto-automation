from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


testusers = {
	"Bobert" : {"fn" : "Bobert", "ln" : "Aardvarkson", "group" : "1"},
	"James" : {"fn" : "James", "ln" : "Jameson", "group" : "2"},
	"Kelly" : {"fn" : "Kelly", "ln" : "Van", "group" : "3"}
}
expectedresults = { 
	"Bobert" : {'fname': 'Bobert', 'lname': 'Aardvarkson', 'prog': '1', 'bonus': '5000.00', 'bweek': '2192.31'},
	"James" : {'fname': 'James', 'lname': 'Jameson', 'prog': '2', 'bonus': '10000.00', 'bweek': '2384.62'},
	"Kelly" : {'fname': 'Kelly', 'lname': 'Van', 'prog': '3', 'bonus': '15000.00', 'bweek': '2576.92'}
	}
# yeah these should be factored out to a variables files as well
# maybe load them in as an array of dictionaries for our test data instead of doing it like this
# it's messy, but it's a mock! 

class HomePage(object):
	#another page class, like in login.py
	def __init__(self, driver):
		self.driver = driver

	def is_title_matches(self):
		"""
		Check that admin dashboard page title is correct, returns True or False
		"""
		return "AbleTo Admin Dashboard" in self.driver.title

	def add_new_employee(self, user):
		"""
		adds a new non-deduction employee in program 1, entering employee details
		"""
		addButton = self.driver.find_element_by_id("btnAddEmployee")
		#easy find because unique button with ID
		addButton.click()
		time.sleep(0.5) # we need to wait for the popup to appear
		fninput = self.driver.find_elements_by_class_name("form-control")[0]
		# these form controls don't have IDs, but their class name is unique so we can just get them by list
		# ideally we'd want to fix that lack of ID problem and specify this better
		# why? because this find method is fragile. if a "form-control" gets added further up
		# we need to bump this all by 1
		fninput.send_keys(testusers[user]["fn"])
		lninput = self.driver.find_elements_by_class_name("form-control")[1]
		lninput.send_keys(testusers[user]["ln"])
		grinput = self.driver.find_elements_by_class_name("form-control")[2]
		grinput.send_keys(testusers[user]["group"])
		#after we send all the keys, we hit the button which has the same id problem and we're good to go 
		submit = self.driver.find_elements_by_class_name("btn-primary")[1]
		submit.click()

	def is_employee_matches(self, row, user):
		"""
		verifies that employee for test case 1 was added and that there's no deduction
		returns True or False
		"""
		tablestring = ".//*[@id='employee-table']/tbody/tr[%s]/td[%s]"
		# this string is used to find the employee table and pick a row and column. 
		# we'll use the column for each value for our return
		# hilariously, this is more robust to changes than the input field because we're using id=employee=table
		# we use string formatters to make life a lot easier
		fname = self.driver.find_elements_by_xpath(tablestring % (row, 2))
		lname = self.driver.find_elements_by_xpath(tablestring % (row, 3))
		prog =  self.driver.find_elements_by_xpath(tablestring % (row, 5))
		bonus =  self.driver.find_elements_by_xpath(tablestring % (row, 7))
		bweek =  self.driver.find_elements_by_xpath(tablestring % (row, 8))
		# we use row to determine which row we want. 2 is the first row that isn't populated yet when we start
		# user fishes a name out of the dictionary up top for expected results. ideally we'd have that in another file or something
		return { "fname" : fname[0].text,
		"lname" : lname[0].text, 
		"prog" : prog[0].text, 
		"bonus" : bonus[0].text, 
		"bweek" : bweek[0].text } == expectedresults[user]
