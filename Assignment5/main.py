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
        COURSES TEXT,
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
    def search_course(self):
        print('\nStudent Search Course Method')

    def add_drop_course(self):
        print('\nStudent Add/Drop Course Method')

    def show_schedule(self):
        print('\nStudent Print Schedule Method')


# Creating Instructor Class
class Instructor(User):
    def __init__(self, first_name, last_name, wentworthID, password, department=None, hire_year=None, email=None):
        super().__init__(first_name, last_name, wentworthID, password)
        self.department = department
        self.hire_year = hire_year
        self.email = email

        if department is None:
            self.department = 'N/A'

        if hire_year is None:
            self.hire_year = 'N/A'

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

    def add_course(self, crn, title, department, time, days, semester, year, credits):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO COURSE VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                       (crn, title, department, time, days, semester, year, credits))
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

    def remove_user(self, wentworthID):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM USER WHERE WENTWORTHID = ?", (wentworthID,))
        conn.commit()
        conn.close()
        print(f"User with Wentworth ID: {wentworthID} removed.")

    def add_student(self, student_id, first_name, last_name, grad_year, major, email):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO STUDENT VALUES (?, ?, ?, ?, ?, ?)",
                       (student_id, first_name, last_name, grad_year, major, email))
        conn.commit()
        conn.close()

    def remove_student(self, wentworthID):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM STUDENT WHERE WENTWORTHID = ?", (wentworthID,))
        conn.commit()
        conn.close()
        print(f"Student with Wentworth ID: {wentworthID} removed.")

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

    def show_roster(self):
        print('\nAdmin Print Roster Method')

    def search_course(self):
        print('\nAdmin Search Course Method')

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
