# Manual work for AbleTo QA test

## Problem statement

### Business Need:

One of the critical functions that we provide is the ability to add employees in our system and manage their pay. Given a set of acceptance criteria, please:

● Write up any bugs found

● Write up 3 test cases

● Choose any test case and automate in the tool of your choice

This is of course a contrived example. We want to know how you would test and automate and get a brief preview of how you work.

### Assumptions:

● All employees have a base salary of $2,000 per paycheck

● There are 26 paychecks in a year

● Each employee is enrolled in a program from 1 to 3

● There is a $5,000 per year bonus for employees enrolled in program #1, $10,000 per year bonus for
employees enrolled in program #2 and $15,000 per year bonus for employees enrolled in program
#3

● The bonus amount is integrated in each paycheck

## Test Cases

### Test Case 1: Adding an Employee without a Deduction
Procedure:
1) Go to login.html
2) Enter admin id and password, then click Login
3) Click Add New Employee
4) Enter First Name, Last Name, and Program, then click Submit
5) Repeat with other 2 test users

Test Data:
1 - First Name: Bobert, Last Name: Aardvarkson, Program: 1
2 - First Name: James, Last Name: Jameson, Program: 2
3 - First Name: Kelly, Last Name: Van, Program: 3

Expected Results:
1) AbleTo login page appears
2) Login should lead to AbleTo Admin Dashboard
3) Add New Employee button should present dialogue
4) Bobert Aardvarkson should appear in table with unique employee ID, program number = 1, base biwieekly pay = 2000.00, program bonus = 5000.00, total biweekly pay = 2192.31
5) James Jameson should appear in table with unique employee ID, program number = 2, base biwieekly pay = 2000.00, program bonus = 10000.00, total biweekly pay = 2384.62
Kelly Van should appear in table with unique employee ID, program number = 3, base biwieekly pay = 2000.00, program bonus = 15000.00, total biweekly pay = 2576.92	

### Test Case 2: Adding an Employee with a deduction
Procedure:
1) Go to login.html
2) Enter admin id and password, then click Login
3) Click Add New Employee
4) Enter First Name, Last Name, and Program, then click Submit
5) Repeat with other 2 test users

Test Data:
1 - First Name: Alice, Last Name: Aardvarkson, Program: 1
2 - First Name: Aaron, Last Name: Jameson, Program: 2
3 - First Name: Andy, Last Name: Van, Program: 3

Expected Results:
1) Ableto login page appears
2) Login should lead to AbleTo Admin Dashboard
3) Add New Employee button should present dialogue
4) Alice Washington should appear in table with unique employee ID, program number = 1, base biweekly pay = 2000.00, program bonus = 4500.00, total biweekly pay = 2173.08
5) Aaron Jameson should appear in table with unique employee ID, program number = 2, base biwieekly pay = 2000.00, program bonus = 9000.00, total biweekly pay = 2346.15
Andy Van should appear in table with unique employee ID, program number = 3, base biwieekly pay = 2000.00, program bonus = 13500.00, total biweekly pay = 2519.23	

### Test Case 3: Deleting an Employee
Procedure:
1) Go to login.html
2) Enter admin id and password, then click Login
3) Click Add New Employee
4) Enter First Name, Last Name, and Program, then click Submit
5) Click the delete button next to the new user.

Expected Results:
1) Ableto login page appears
2) Login should lead to AbleTo Admin Dashboard
3) Add New Employee button should present dialogue
4) A new user should appear in the table.
5) The employee entry should disappear from the table


## Bugs

### Bug: Employee IDs do not increment
#### Description
When adding a new employee, ID is always 1 and cannot be changed
#### Procedure
Add a new employee
#### Expected Result:
New employee is added with a unique ID
#### Actual Result:
Employee is added with an ID of 1

### Bug: Invalid Program number input is accepted
#### Description
When adding a new employee, invalid program number inputs, such as large numbers or letters, are incorrectly allowed
#### Procedure
Add a new employee and put in an invalid program number, such as a non-numeric input, or an integer other than 1, 2, or 3, or nothing.
#### Expected Result:
Submission of employee is blocked, or forced to put in a valid input, or defaults to a number (depends on our business case here)
#### Actual Result:
Incorrect input is allowed. When the input is a number, it incorrect assigns a program bonus (such as 7500.00 for a program 1.5)

### Bug: Invalid name input is accepted
#### Description
When adding a new employee, invalid name inputs, such as leaving the name completely blank, are allowed.
#### Procedure
Add a new employee and put in an invalid name input for first name or last name, empty strings.
#### Expected Result:
Submission of employee is blocked unless employee first and last name are both strings of length at least 1
#### Actual Result:
Any input, including completely empty input, is allowed.

### Bug: All data is lost on refresh
#### Description
All data is lost on refresh except for Kevin Moore. Is this a test env issue?
#### Procedure
Add a new employee then refresh the page
#### Expected Result:
New employee persists
#### Actual Result:
Table is reset to just have Kevin Moore

### Bug: All data is lost on refresh
#### Description
All data is lost on refresh except for Kevin Moore. Is this a test env issue?
#### Procedure
Add a new employee then refresh the page
#### Expected Result:
New employee persists
#### Actual Result:
Table is reset to just have Kevin Moore

### Bug: UI isn't locked during user delete
#### Description
During user deletion, the UI isn't locked, allowing inputs that can cause incorrect entries to be deleted. Also, new deletions can be started while one is in progress, causing multiple overlapping spinners to appear.
#### Procedure
Add a few users, then delete one. While that user is being deleted, and the spinner is spinning, add a new user 
#### Expected Result:
The UI should be inoperable during user deletion. Alternatively, if we wish for the UI to be operable, adding a new user should work safely and shouldn't disrupt the deletion operation
#### Actual Result:
Adding a new user results in the new user being deleted instead of the selected user to delete. It seems like it may be possible to cause other problems with renaming

### Bug: Long name stretches Name Column
#### Description
Entering a very long last name stretches the last name column, causing the table to be illegible
#### Procedure
Add a new user with a very long name, 50 or more characters.
#### Expected Result:
The user's name should be accommodated with a suitable max length, beyond which the column no longer expands in order to preserve table visibility. The individual column could become scrollable or partially occluded, or we could choose not to accept names beyond a certain length. 
#### Actual Result:
Last names can be very long and make the column very wide until it is the only visible element in the pane.

