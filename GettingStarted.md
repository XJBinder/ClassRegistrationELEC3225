# Python Registration System
***Jon Binder  &&  Ayush Sharma  &&  Carson Mershon***

This is our ELEC3225 Class Registration Software. This code uses SQLite3 to create and perform operations on a database. The database stores user and course information. Different types of users can perform different commands on the database based on their level of authority.

## Features
**User Class**:
- Search Courses
- Display All Courses
- Show Account Information
- Change Password

**Student Class**:
- Search Courses
- Display All Courses
- Add/Drop Courses to and from Schedule
- Display Students Schedule
- Show Account Information
- Change Password

**Instructor Class**:
- Search Courses
- Display All Courses
- Search Class Roster
- Display Class Roster
- Show Account Information
- Change Password

**Admin Class**:
- Search Courses
- Display All Courses
- Search Class Roster
- Display Class Roster
- Add/Remove a Course from the Database
- Add/Remove a User from the Database
- Add/Remove a Student from the Database
- Add/Remove a Instructor from the Database
- Add/Remove Admins from the Database
- Update Admin Information
- Show Account Information
- Change Password

## Prerequisites
- Python 3.0 or later
- DatabaseGenerator.py is optional (run to create example database.db)

## Installation
After downloading the latest version of Python (3.12.4 as of August 2024)
1. Download main.py
2. Run main.py using an IDE, Terminal, or your favorite way to run Python Scripts
 
#### Command Prompt Method
*Ensure Python is installed*
```sh
python --version
```
or
```sh
python3 --version
```
or
```sh
py --version
```

*Navigate to main.py directory*
```sh
cd C:\Users\YourUser\DownloadLocation
```

*Run main.py*
```sh
python main.py
```

## Example Demonstration

*You will be greeted with a Welcome Menu*
```sh
---Welcome to Leopard Web Class Registration Software---
1. Login
2. Create Account
3. Exit
Select an Option: 2
```

*For this example I will choose to create an account*
```sh
---Account Type---
1. Student
2. Instructor
3. Admin
4. Parent/Other (User)
Select an Option: 1
```

*Next I will create a Student account*
```sh
--Create Student Account--
Enter your First Name: Danny
Enter your Last Name: Dorito
Enter your Wentworth ID: W11171944
Enter your Password: m&ms4lfE
Enter your Graduation Year: 2025
Enter your Major: BSEE
Enter your Email: dannyd@wit.edu

--Student Menu--
1. Search Course
2. Show All Courses
3. Add Course
4. Drop Course
5. Show Schedule
6. Show My Info
7. Change Password
8. Exit
Select an Option: 2
```
*Here I entered my information and an account was created in the database*
*The Student Selection Menu pops up and I will choose to Show All Courses*

```sh
(10000, 'Intro to Walking', 'BSEE', '1530', 'MWF', 'Summer', 2024, 4)
(10001, 'How to Breathe', 'BSCE', '1530', 'MWF', 'Summer', 2024, 4)
(10002, 'Advanced Procrastination', 'BSCE', '0900', 'MWF', 'Fall', 2024, 3)
...
(10007, 'Introduction to Nap Taking', 'BSEE', '1200', 'TTH', 'Fall', 2024, 3)
```

*Next I will try adding a Course to my schedule*
```sh
...
3. Add Course
4. Drop Course
5. Show Schedule
6. Show My Info
7. Change Password
8. Exit
Select an Option: 3

--Add Course--
Enter CRN (or 'exit' to cancel): 10007
Course 10007 added.
```

*Now I will show my schedule*
```sh
...
5. Show Schedule
6. Show My Info
7. Change Password
8. Exit
Select an Option: 5
Course Name: Introduction to Nap Taking, Course Time: 1200, Course Days: TTH
```

*What happens if I enter something wrong?*
```sh
Select an Option: notaNumb3r
Invalid Entry
Select an Option: 3

--Add Course--
Enter CRN (or 'exit' to cancel): somethingRandom4123?
CRN must be a number.
Enter CRN (or 'exit' to cancel): 31245325
Course with CRN 31245325 does not exist.
Enter CRN (or 'exit' to cancel): exIT

--Student Menu--
...
```
