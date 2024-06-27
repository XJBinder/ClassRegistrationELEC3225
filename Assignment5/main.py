import sqlite3


def create_COURSE_table():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    # Create new table called "COURSE"
    cursor.execute('''CREATE TABLE IF NOT EXISTS COURSE (
        CRN INTEGER PRIMARY KEY,
        TITLE TEXT NOT NULL,
        DEPARTMENT TEXT NOT NULL,
        TIME TEXT NOT NULL,
        DAYS TEXT NOT NULL,
        SEMESTER TEXT NOT NULL,
        YEAR INTEGER NOT NULL,
        CREDITS INTEGER NOT NULL)''')

    conn.commit()
    conn.close()


def create_USER_table():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    # Create new table called "USER"
    cursor.execute('''CREATE TABLE IF NOT EXISTS USER (
        WENTWORTHID INTEGER PRIMARY KEY,
        FIRSTNAME TEXT NOT NULL,
        LASTNAME TEXT NOT NULL,
        PASSWORD TEXT NOT NULL)''')

    conn.commit()
    conn.close()


def create_STUDENT_table():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    # Create new table called "STUDENT"
    cursor.execute('''CREATE TABLE IF NOT EXISTS STUDENT (
        WENTWORTHID INTEGER PRIMARY KEY,
        FIRSTNAME TEXT NOT NULL,
        LASTNAME TEXT NOT NULL,
        PASSWORD TEXT NOT NULL,
        COURSES INTEGER,
        GRADYEAR INTEGER,
        MAJOR TEXT,
        EMAIL TEXT)''')

    conn.commit()
    conn.close()


def create_ADMIN_table():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    # Create new table called "ADMIN"
    cursor.execute('''CREATE TABLE IF NOT EXISTS ADMIN (
        WENTWORTHID INTEGER PRIMARY KEY,
        FIRSTNAME TEXT NOT NULL,
        LASTNAME TEXT NOT NULL,
        PASSWORD TEXT NOT NULL,
        TITLE TEXT,
        OFFICE TEXT,
        EMAIL TEXT)''')

    conn.commit()
    conn.close()


def create_INSTRUCTOR_table():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    # Create new table called "INSTRUCTOR"
    cursor.execute('''CREATE TABLE IF NOT EXISTS INSTRUCTOR (
        WENTWORTHID INTEGER PRIMARY KEY,
        FIRSTNAME TEXT NOT NULL,
        LASTNAME TEXT NOT NULL,
        PASSWORD TEXT NOT NULL,
        DEPARTMENT TEXT,
        HIREYEAR INTEGER,
        TITLE TEXT,
        EMAIL TEXT)''')

    conn.commit()
    conn.close()


# Creating User Class
class User:
    def __init__(self, first_name, last_name, wentworthID, password):
        self.first_name = first_name
        self.last_name = last_name
        self.wentworthID = wentworthID
        self.password = password

    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_wentworthID(self, wentworthID):
        self.wentworthID = wentworthID

    def set_password(self, password):
        self.password = password

    def show_all_info(self):
        return 'Firstname:{}, Lastname:{}, Wentworth ID:{},'.format(self.first_name, self.last_name, self.wentworthID)


# Creating Student Class
class Student(User):
    def __init__(self, first_name, last_name, wentworthID, password, courses=None, grad_year=None, major=None, email=None):
        super().__init__(first_name, last_name, wentworthID, password)
        self.courses = courses
        self.grad_year = grad_year
        self.major = major
        self.email = email

        if courses is None:
            self.courses = 'N/A'

        if grad_year is None:
            self.grad_year = 'N/A'

        if major is None:
            self.major = 'N/A'

        if email is None:
            self.email = 'N/A'

    def search_course(self):
        print('\nStudent Search Course Method')

    def add_course(self):
        print('\nStudent Add Course Method')

    def drop_course(self):
        print('\nStudent Drop Course Method')

    def show_schedule(self):
        print('\nStudent Print Schedule Method')


# Creating Instructor Class
class Instructor(User):
    def __init__(self, first_name, last_name, wentworthID, password, department=None, hire_year=None, title=None, email=None):
        super().__init__(first_name, last_name, wentworthID, password)
        self.department = department
        self.hire_year = hire_year
        self.title = title
        self.email = email

        if department is None:
            self.department = 'N/A'

        if hire_year is None:
            self.hire_year = 'N/A'

        if title is None:
            self.title = 'N/A'

        if email is None:
            self.email = 'N/A'


# Creating Admin Class
class Admin(User):
    def __init__(self, first_name, last_name, wentworthID, password, title=None, office=None, email=None):
        super().__init__(first_name, last_name, wentworthID, password)
        self.title = title
        self.office = office
        self.email = email

        if title is None:
            self.title = 'N/A'

        if office is None:
            self.office = 'N/A'

        if email is None:
            self.email = 'N/A'

    def add_course(self, crn, title, department, time, days, semester, year, credit):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO COURSE VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                       (crn, title, department, time, days, semester, year, credit))
        conn.commit()
        conn.close()
        print(f"Course {title} added.")

    def remove_course(self, crn):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM COURSE WHERE CRN = ?", (crn,))
        conn.commit()
        conn.close()
        print(f"Course with CRN {crn} removed.")

    def add_user(self, wentworthID, first_name, last_name, password):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO USER VALUES (?, ?, ?, ?)",
                       (wentworthID, first_name, last_name, password))
        conn.commit()
        conn.close()
        print(f"User with Wentworth ID: {wentworthID} added.")

    def remove_user(self, wentworthID):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM USER WHERE WENTWORTHID = ?", (wentworthID,))
        conn.commit()
        conn.close()
        print(f"User with Wentworth ID: {wentworthID} removed.")

    def add_student(self, wentworthID, first_name, last_name, password, courses, grad_year, major, email):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO STUDENT VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                       (wentworthID, first_name, last_name, password, courses, grad_year, major, email))
        conn.commit()
        conn.close()
        print(f"Student with Wentworth ID: {wentworthID} added.")

    def remove_student(self, wentworthID):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM STUDENT WHERE WENTWORTHID = ?", (wentworthID,))
        conn.commit()
        conn.close()
        print(f"Student with Wentworth ID: {wentworthID} removed.")

    def add_instructor(self, wentworthID, first_name, last_name, password, department, hire_year, title, email):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO INSTRUCTOR VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                       (wentworthID, first_name, last_name, password, department, hire_year, title, email))
        conn.commit()
        conn.close()
        print(f"Instructor with Wentworth ID: {wentworthID} added.")

    def remove_instructor(self, wentworthID):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM INSTRUCTOR WHERE WENTWORTHID = ?", (wentworthID,))
        conn.commit()
        conn.close()
        print(f"Instructor with Wentworth ID: {wentworthID} removed.")

    def add_admin(self, wentworthID, first_name, last_name, password, title, office, email):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO ADMIN VALUES (?, ?, ?, ?, ?, ?, ?)",
                       (wentworthID, first_name, last_name, password, title, office, email))
        conn.commit()
        conn.close()
        print(f"Admin with Wentworth ID: {wentworthID} added.")

    def remove_admin(self, wentworthID):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM ADMIN WHERE WENTWORTHID = ?", (wentworthID,))
        conn.commit()
        conn.close()
        print(f"Admin with Wentworth ID: {wentworthID} removed.")

    def query_users(self):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM USER")
        admins = cursor.fetchall()
        for user in users:
            print(user)
        conn.close()

    def query_students(self):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM STUDENT")
        students = cursor.fetchall()
        for student in students:
            print(student)
        conn.close()

    def query_instructors(self):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM INSTRUCTOR")
        instructors = cursor.fetchall()
        for instructor in instructors:
            print(instructor)
        conn.close()

    def query_admins(self):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM ADMIN")
        admins = cursor.fetchall()
        for admin in admins:
            print(admin)
        conn.close()

    def search_roster(self):
        print('\nAdmin Search Roster Method')

    def print_roster(self, crn):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        # Print Course Title based on CRN
        cursor.execute("""
            SELECT TITLE
            FROM COURSE
            WHERE CRN = ?
        """, (crn,))
        title = cursor.fetchone()[0]
        print(f"Roster for {title}:")

        # Query to find the department of the inputted course
        cursor.execute("""
            SELECT DEPARTMENT
            FROM COURSE
            WHERE CRN = ?
        """, (crn,))
        dept = cursor.fetchone()[0]

        # Query to find all instructors that have the inputted course
        cursor.execute("""
                    SELECT INSTRUCTOR.*, COURSE.*
                    FROM INSTRUCTOR
                    JOIN COURSE ON INSTRUCTOR.DEPARTMENT = COURSE.DEPARTMENT
                    WHERE COURSE.DEPARTMENT = ?
                """, (dept,))
        instructors_with_course = cursor.fetchall()
        print("Instructors that can teach this course:")
        for instructor in instructors_with_course:
            print(instructor)

        # Query to find all students that have the inputted course
        cursor.execute("""
            SELECT STUDENT.*, COURSE.*
            FROM STUDENT
            JOIN COURSE ON STUDENT.COURSES = COURSE.CRN
            WHERE COURSE.CRN = ?
        """, (crn,))
        students_with_course = cursor.fetchall()
        print(f"Students taking {title}:")
        for student in students_with_course:
            print(student)

        conn.close()

    def search_course(title=None, day=None, time=None):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        query = "SELECT * FROM COURSE WHERE 1"
        params = []

        if title is not None:
            query += " AND TITLE LIKE ?"
            params.append('%' + str(title) + '%')

        if day is not None:
            query += " AND DAYS LIKE ?"
            params.append('%' + day + '%')

        if time is not None:
            query += " AND TIME LIKE ?"
            params.append('%' + time + '%')

        cursor.execute(query, params)

        courses = cursor.fetchall()
        for course in courses:
            print(course)

        conn.close()

    def show_course(self):
        print('\nAdmin Print Course Method')

    def update_admin(self, admin_id, new_title):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE ADMIN SET TITLE = ? WHERE ID = ?", (new_title, admin_id))
        conn.commit()
        conn.close()
        print(f"Admin with ID {admin_id} updated to {new_title}.")

    def remove_instructor(self, instructor_id):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM INSTRUCTOR WHERE ID = ?", (instructor_id,))
        conn.commit()
        conn.close()
        print(f"Instructor with ID {instructor_id} removed.")


create_COURSE_table()
create_USER_table()
create_STUDENT_table()
create_INSTRUCTOR_table()
create_ADMIN_table()

# Welcome
# Login or Create Account
# If Login: Enter Wentworth ID and Password

# If Create Account: Enter First Name, Last Name, Wentworth ID, Password, and Account Type
# Account Types: Parent/Other, Student, Instructor, Admin
# If Student: Enter Graduation Year, Major, and Email
# If Instructor: Enter Department, Hire Year, and Email
# If Admin: Enter Title, Office, and Email

# If Student: Search Course, Add/Drop Course, Show Schedule
# If Instructor: Search Roster, Show Roster, Search Course, Show Course
# If Admin: Search Roster, Show Roster, Search Course, Show Course, Add Course, Remove Course, Add User,
# Remove User, Add Student, Remove Student, Query Students, Query Instructors, Query Admins, Update Admin,
# Remove Instructor

#
