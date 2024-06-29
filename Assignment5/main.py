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


def login(wentworthID, password):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # List of tables to check
    tables = ['USER', 'STUDENT', 'INSTRUCTOR', 'ADMIN']
    account_exists = False

    for table in tables:
        cursor.execute(f"SELECT * FROM {table} WHERE WENTWORTHID = ?", (wentworthID,))
        account = cursor.fetchone()

        if account is not None:
            account_exists = True
            if account[3] != password:
                print("Password Incorrect")
                break
            else:
                print(f"Logged in as {account[1]}")
                return account, table

    if not account_exists:
        print("Account does not exist")

    conn.close()


def main_menu():
    run_menu = True
    user = 4  # A Number that is not 0, 1, 2, or 3

    while True:
        try:
            if run_menu:
                run_menu = False
                print("-----Main Menu-----")
                print("---Welcome to Leopard Web Class Registration Software---")
                print("1. Login")
                print("2. Create Account")

            choice = input("Enter your Choice: ")

            if choice == '1':
                print("---Login---")
                wentworthID = input("Enter your Wentworth ID: ")
                password = input("Enter your Password: ")
                fetched_account, fetched_account_type = login(wentworthID, password)

                if fetched_account_type == 'USER':
                    user = 0
                    user_object = User(fetched_account[1], fetched_account[2], fetched_account[0], fetched_account[3])
                elif fetched_account_type == 'STUDENT':
                    user = 1
                    user_object = Student(fetched_account[1], fetched_account[2], fetched_account[0],
                                          fetched_account[3], fetched_account[4], fetched_account[5],
                                          fetched_account[6], fetched_account[7])
                elif fetched_account_type == 'INSTRUCTOR':
                    user = 2
                    user_object = Instructor(fetched_account[1], fetched_account[2], fetched_account[0],
                                             fetched_account[3], fetched_account[4], fetched_account[5],
                                             fetched_account[6], fetched_account[7])
                elif fetched_account_type == 'ADMIN':
                    user = 3
                    user_object = Admin(fetched_account[1], fetched_account[2], fetched_account[0],
                                        fetched_account[3], fetched_account[4], fetched_account[5],
                                        fetched_account[6])
            elif choice == '2':
                print("---Account Type---")
                print("1. Student")
                print("2. Instructor")
                print("3. Admin")
                print("4. Parent/Other (User)")
                while True:
                    try:
                        account_type = int(input("Enter a number: "))
                        if not 1 <= account_type <= 4:
                            print("Invalid Entry")
                            continue
                        else:
                            break
                    except ValueError:
                        print("Invalid Entry")

                # If User is Selected
                if account_type == 4:
                    # Ask for firstname, lastname, Wentworth ID, Password
                    user = 0
                    first_name = input("Enter your First Name: ")
                    last_name = input("Enter your Last Name: ")
                    wentworthID = input("Enter your Wentworth ID: ")
                    password = input("Enter your Password: ")

                    # CREATE USER OBJECT

                # If Student is Selected
                elif account_type == 1:
                    # Ask for firstname, lastname, wentworth ID, password, Graduation Year, Major, Email
                    user = 1
                    first_name = input("Enter your First Name: ")
                    last_name = input("Enter your Last Name: ")
                    wentworthID = input("Enter your Wentworth ID: ")
                    password = input("Enter your Password: ")
                    grad_year = input("Enter your Graduation Year: ")
                    major = input("Enter your Major: ")
                    email = input("Enter your Email: ")

                    # CREATE STUDENT OBJECT

                # If Instructor is Selected
                elif account_type == 2:
                    # Ask for firstname, lastname, wentworth ID, password, Department, Hire Year, Title, Email
                    user = 2
                    first_name = input("Enter your First Name: ")
                    last_name = input("Enter your Last Name: ")
                    wentworthID = input("Enter your Wentworth ID: ")
                    password = input("Enter your Password: ")
                    department = input("Enter your Department: ")
                    hire_year = input("Enter your Hire Year: ")
                    title = input("Enter your Title: ")
                    email = input("Enter your Email: ")

                    # CREATE INSTRUCTOR OBJECT

                # If Admin is Selected
                elif account_type == 3:
                    # Ask for firstname, lastname, wentworth ID, password, Title, Office, Email
                    user = 3
                    first_name = input("Enter your First Name: ")
                    last_name = input("Enter your Last Name: ")
                    wentworthID = input("Enter your Wentworth ID: ")
                    password = input("Enter your Password: ")
                    title = input("Enter your Title: ")
                    office = input("Enter your Office: ")
                    email = input("Enter your Email: ")

                    # CREATE ADMIN OBJECT

            else:
                print("Invalid Entry")

            if user == 0:  # USER
                print("USER MENU ITEMS")
                print("1. Search Course")
                print("2. Show User Info")
                print("3. Change Password")
                # Search Course, Show User Info, change password
            elif user == 1:  # STUDENT
                print("STUDENT MENU ITEMS")
                print("1. Search Course")
                print("2. Add Course")
                print("3. Drop Course")
                print("4. Show Schedule")
                print("5. Show Course")
                print("6. Show User Info")
                print("7. Change Password")
                # Search Course, Add Course, Drop Course, Show Schedule, show course, show user info, change password
            elif user == 2:  # INSTRUCTOR
                print("INSTRUCTOR MENU ITEMS")
                print("1. Search Roster")
                print("2. Show Roster")
                print("3. Seach Course")
                print("4. Show Course")
                print("5. Show Schedule")
                print("6. Show User Info")
                print("7. Change Password")
                # Search Roster, Show Roster, Search Course, Show Course, show schedule, show user info, change password
            elif user == 3:  # ADMIN
                print("ADMIN MENU ITEMS")
                print("1. Search Roster")
                print("2. Show Roster")
                print("3. Search Course")
                print("4. Show Course")
                print("5. Add Course")
                print("6, Remove Course")
                print("7. Add User")
                print("8. Remove User")
                print("9. Add Student")
                print("10. Remove Student")
                print("11. Add Instructor")
                print("12. Remove Instructor")
                print("13. Add Admin")
                print("14. Remove Admin")
                print("15. Query Users")
                print("16. Query Students")
                print("17. Query Instructors")
                print("18. Query Admins")
                print("19. Update Admin")
                print("20. Show User Info")
                print("21. Change Password")
            # Search Roster, Show Roster, Search Course, Show Course, Add Course, Remove Course, Add User,
            # Remove User, Add Student, Remove Student, Add Instructor, Remove Instructor, Add Admin, Remove Admin,
            # Query Users, Query Students, Query Instructors, Query Admins, Update Admin, show user info,
            # change password

                                                ## AYUSH ##
            #       Im not sure is this is everything we need to do.. if you could check the requirements and add more
            #         if needed that would be sweet.. im thinking I will need to add more functions to the classes so
            #         dont worry about checking to see if they are all there.. just add based on the assignment doc
            #         and add those print statements to the menu items, thanks cutie <3

        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            input("Press Enter to continue...")


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

    def search_course(crn=None, title=None, day=None, time=None):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        query = "SELECT * FROM COURSE WHERE 1"
        params = []

        if crn is not None:
            query += " AND CRN LIKE ?"
            params.append('%' + crn + '%')

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


# Creating Student Class
class Student(User):
    def __init__(self, first_name, last_name, wentworthID, password, courses=None, grad_year=None, major=None,
                 email=None):
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

    def add_course(self):
        print('\nStudent Add Course Method')

    def drop_course(self):
        print('\nStudent Drop Course Method')

    def show_schedule(self):
        print('\nStudent Print Schedule Method')


# Creating Instructor Class
class Instructor(User):
    def __init__(self, first_name, last_name, wentworthID, password, department=None, hire_year=None, title=None,
                 email=None):
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

    def query_courses(self):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM COURSE")
        courses = cursor.fetchall()
        for course in courses:
            print(course)
        conn.close()

    def query_users(self):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM USER")
        users = cursor.fetchall()
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

    def search_roster(self, crn):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        # Find the course with the given CRN
        cursor.execute("SELECT * FROM COURSE WHERE CRN = ?", (crn,))
        course = cursor.fetchone()
        if course is None:
            print(f"No course found with CRN {crn}")
            return
        else:
            title = course[1]
            print(f"{title} Roster Search:")
            wentworthID = input("Enter Wentworth ID:")

        # Find the student with the given WentworthID
        cursor.execute("SELECT * FROM STUDENT WHERE WENTWORTHID = ?", (wentworthID,))
        student = cursor.fetchone()
        if student is not None:
            student_obj = Student(student[1], student[2], student[0], student[3], student[4], student[5],
                                  student[6], student[7])
            print(student_obj.show_all_info())
            return

        # Find the instructor with the given WentworthID
        cursor.execute("SELECT * FROM INSTRUCTOR WHERE WENTWORTHID = ?", (wentworthID,))
        instructor = cursor.fetchone()
        if instructor is not None:
            instructor_obj = Instructor(instructor[1], instructor[2], instructor[0], instructor[3], instructor[4],
                                        instructor[5], instructor[6], instructor[7])
            print(instructor_obj.show_all_info())
            return

        print(f"No user found with Wentworth ID {wentworthID}")

        conn.close()

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

    def update_admin(self, admin_id, new_title):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE ADMIN SET TITLE = ? WHERE ID = ?", (new_title, admin_id))
        conn.commit()
        conn.close()
        print(f"Admin with ID {admin_id} updated to {new_title}.")

        conn.commit()
        conn.close()


if __name__ == '__main__':
    create_COURSE_table()
    create_USER_table()
    create_STUDENT_table()
    create_INSTRUCTOR_table()
    create_ADMIN_table()

    main_menu()
